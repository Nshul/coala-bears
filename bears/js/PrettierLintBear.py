
from coalib.bearlib.abstractions.Linter import linter
from dependency_management.requirements.NpmRequirement import NpmRequirement


@linter(executable='prettier',
        use_stdout=True,
        use_stderr=True)
class PrettierLintBear:
    """
    Formats JavaScript,JSX,Flow,TypeScript,CSS,Less,SCSS,JSON,GraphQL,Markdown
    files according to opinionated code format
    using ``prettier``.

    See <https://github.com/prettier/prettier> for more information.
    """
    LANGUAGES = {'JavaScript'}
    REQUIREMENTS = {NpmRequirement('prettier', '1')}
    AUTHORS = {'The coala developers'}
    AUTHORS_EMAILS = {'coala-devel@googlegroups.com'}
    LICENSE = 'AGPL-3.0'
    CAN_DETECT = {'Consistency', 'Correctness', 'Whitespace',
                  'Parentheses', 'Strings', 'Empty lines',
                  'Multi-line objects'}
    SEE_MORE = 'https://prettier.io/'

    def process_output(self, output, filename, file):
        stdout, stderr = output
        regex = r'L(?P<line>\d+)C(?P<column>\d+): (?P<message>.*)'
        yield from self.process_output_corrected(stdout, filename, file)
        yield from self.process_output_regex(stderr, filename, file, regex)

    @classmethod
    def create_arguments(cls, filename, file, config_file):
        return filename,
