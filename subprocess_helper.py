import sys
import subprocess

from typing import Optional, Union, TextIO, BinaryIO, List

from logger import CustomLogger

class NonZeroCodeException(Exception):
    pass


class SubprocessHelper:
    def __init__(self, logger: CustomLogger) -> None:
        self._logger = logger

    def run(self,
            cmd: list,
            stdin: Union[TextIO, BinaryIO, None] = None,
            interactive_output: bool = False,
            env: Optional[dict] = None,
            chdir: Optional[str] = None,
            save_to_file: Optional[str] = None,
            rc_excludes: List[int] = [],
            shell=True) -> str:

        stdout = subprocess.PIPE
        stderr = subprocess.PIPE

        if interactive_output:
            stdout = sys.stdout
            stderr = sys.stderr

        if save_to_file:
            stdout = open(save_to_file, 'w')

        self._logger.debug(f'running subprocess: {cmd}')

        process = subprocess.run(cmd, stderr=stderr, stdout=stdout, stdin=stdin, env=env, cwd=chdir, shell=shell)

        if process.returncode not in [0, *rc_excludes]:
            error = f'subprocess {cmd} returned "{process.returncode}" exit code!'

            if not interactive_output:
                if save_to_file:
                    error = (
                        f'{error}\n\n'
                        f'subprocess stderr:\n{process.stderr.decode("utf-8")}\n'
                    )
                else:
                    error = (
                        f'{error}\n\n'
                        f'subprocess stderr:\n{process.stderr.decode("utf-8")}\n\n'
                        f'subprocess stdout:\n{process.stdout.decode("utf-8")}\n'
                    )

            raise NonZeroCodeException(error)

        if save_to_file:
            stdout.close()

        self._logger.debug(f'subprocess {cmd} exited')

        if not process.stdout:
            return ''

        return process.stdout.decode('utf-8')
