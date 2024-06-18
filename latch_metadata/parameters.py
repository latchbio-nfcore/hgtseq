
from dataclasses import dataclass
import typing
import typing_extensions

from flytekit.core.annotation import FlyteAnnotation

from latch.types.metadata import NextflowParameter
from latch.types.file import LatchFile
from latch.types.directory import LatchDir, LatchOutputDir

# Import these into your `__init__.py` file:
#
# from .parameters import generated_parameters

generated_parameters = {
    'input': NextflowParameter(
        type=LatchFile,
        default=None,
        section_title='Input/output options',
        description='Path to comma-separated file containing information about the samples in the experiment.',
    ),
    'outdir': NextflowParameter(
        type=typing_extensions.Annotated[LatchDir, FlyteAnnotation({'output': True})],
        default=None,
        section_title=None,
        description='The output directory where the results will be saved. You have to use absolute paths to storage on Cloud infrastructure.',
    ),
    'email': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Email address for completion summary.',
    ),
    'multiqc_title': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='MultiQC report title. Printed as page header, used for filename if not otherwise specified.',
    ),
    'isbam': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Indicates if input files are BAMs: if not, FASTQ files are assumed and alignment is run',
    ),
    'taxonomy_id': NextflowParameter(
        type=float,
        default=None,
        section_title=None,
        description='TaxID of samples used as input',
    ),
    'aligner': NextflowParameter(
        type=typing.Optional[str],
        default='bwa-mem',
        section_title='Run options',
        description='Choose if aligner should be bwa-mem or bwa-mem2',
    ),
    'genome': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title='Reference genome options',
        description='Name of iGenomes reference.',
    ),
    'krakendb': NextflowParameter(
        type=str,
        default='None',
        section_title=None,
        description='A local path to kraken database folder or compressed database file, or a URL to a compressed database file, in tar.gz format',
    ),
    'kronadb': NextflowParameter(
        type=str,
        default='None',
        section_title=None,
        description='A local path or a URL to a .tab krona taxonomy file; it can also receive a compressed .tab file in tar.gz format',
    ),
    'multiqc_methods_description': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title='Generic options',
        description='Custom MultiQC yaml file containing HTML including a methods description.',
    ),
}

