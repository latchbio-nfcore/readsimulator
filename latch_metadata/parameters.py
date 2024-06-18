
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
    'amplicon': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title='Simulation options',
        description='Option to simulate amplicon sequencing reads.',
    ),
    'target_capture': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Option to simulate target capture sequencing reads.',
    ),
    'metagenome': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Option to simulate metagenomic sequencing reads.',
    ),
    'wholegenome': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Option to simulate wholegenomic sequencing reads.',
    ),
    'amplicon_fw_primer': NextflowParameter(
        type=typing.Optional[str],
        default='GTCGGTAAAACTCGTGCCAGC',
        section_title='Amplicon options',
        description='Forward primer to use with crabs_insilicopcr.',
    ),
    'amplicon_rv_primer': NextflowParameter(
        type=typing.Optional[str],
        default='CATAGTGGGGTATCTAATCCCAGTTTG',
        section_title=None,
        description='Reverse primer to use with crabs_insilicopcr.',
    ),
    'amplicon_read_count': NextflowParameter(
        type=typing.Optional[int],
        default=500,
        section_title=None,
        description='Number of reads to be simulated per amplicon.',
    ),
    'amplicon_read_length': NextflowParameter(
        type=typing.Optional[int],
        default=130,
        section_title=None,
        description='Length of reads to be simulated.',
    ),
    'amplicon_seq_system': NextflowParameter(
        type=typing.Optional[str],
        default='HS25',
        section_title=None,
        description='Sequencing system of reads to be simulated.',
    ),
    'amplicon_crabs_ispcr_error': NextflowParameter(
        type=typing.Optional[float],
        default=4.5,
        section_title=None,
        description='Maximum number of errors allowed in CRABS insilicoPCR primer sequences',
    ),
    'probe_file': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title='Target capture options',
        description='Path to bait/probe file. Can be a fasta file or a bed file.',
    ),
    'probe_ref_name': NextflowParameter(
        type=typing.Optional[str],
        default='Tetrapods-UCE-5Kv1',
        section_title=None,
        description='Name of supported probe. Mandatory if not using `--probes` parameter.',
    ),
    'target_capture_mode': NextflowParameter(
        type=typing.Optional[str],
        default='illumina',
        section_title=None,
        description="Simulate 'illumina' or 'pacbio' reads.",
    ),
    'target_capture_fmedian': NextflowParameter(
        type=typing.Optional[int],
        default=500,
        section_title=None,
        description='Median of fragment size at shearing.',
    ),
    'target_capture_fshape': NextflowParameter(
        type=typing.Optional[float],
        default=6,
        section_title=None,
        description='Shape parameter of the fragment size distribution.',
    ),
    'target_capture_smedian': NextflowParameter(
        type=typing.Optional[int],
        default=1300,
        section_title=None,
        description='Median of fragment size distribution.',
    ),
    'target_capture_sshape': NextflowParameter(
        type=typing.Optional[float],
        default=6,
        section_title=None,
        description='Shape parameter of the fragment size distribution.',
    ),
    'target_capture_tmedian': NextflowParameter(
        type=typing.Optional[int],
        default=None,
        section_title=None,
        description="Median of target fragment size (the fragment size of the data). If specified, will override '--fmedian' and '--smedian'. Othersise will be estimated.",
    ),
    'target_capture_tshape': NextflowParameter(
        type=typing.Optional[float],
        default=None,
        section_title=None,
        description='Shape parameter of the effective fragment size distribution.',
    ),
    'target_capture_num': NextflowParameter(
        type=typing.Optional[int],
        default=500000,
        section_title=None,
        description='Number of fragments.',
    ),
    'target_capture_illen': NextflowParameter(
        type=typing.Optional[int],
        default=150,
        section_title=None,
        description='Illumina: read length.',
    ),
    'target_capture_pblen': NextflowParameter(
        type=typing.Optional[int],
        default=30000,
        section_title=None,
        description='PacBio: Average (polymerase) read length.',
    ),
    'target_capture_ilmode': NextflowParameter(
        type=typing.Optional[str],
        default='pe',
        section_title=None,
        description='Illumina: Sequencing mode.',
    ),
    'metagenome_abundance': NextflowParameter(
        type=typing.Optional[str],
        default='lognormal',
        section_title='Metagenome options',
        description='Abundance distribution.',
    ),
    'metagenome_abundance_file': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Path to tab-separated file containing abundance distribution.',
    ),
    'metagenome_coverage': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Coverage distribution.',
    ),
    'metagenome_coverage_file': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Path to tab-separated file containing coverage information.',
    ),
    'metagenome_input_format': NextflowParameter(
        type=typing.Optional[str],
        default='genomes',
        section_title=None,
        description='Format of FASTA file used to generate reads',
    ),
    'metagenome_n_reads': NextflowParameter(
        type=typing.Optional[str],
        default='1M',
        section_title=None,
        description='Number of reads to generate.',
    ),
    'metagenome_mode': NextflowParameter(
        type=typing.Optional[str],
        default='kde',
        section_title=None,
        description="Can be 'kde', or 'basic'.",
    ),
    'metagenome_model': NextflowParameter(
        type=typing.Optional[str],
        default='MiSeq',
        section_title=None,
        description="Can be 'HiSeq', 'NovaSeq', or 'MiSeq'.",
    ),
    'metagenome_gc_bias': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Use this option to prevent simulating reads that have abnormal GC content.',
    ),
    'wholegenome_error_rate': NextflowParameter(
        type=typing.Optional[float],
        default=0.02,
        section_title='Wholegenome options',
        description='The base error rate.',
    ),
    'wholegenome_outer_dist': NextflowParameter(
        type=typing.Optional[int],
        default=500,
        section_title=None,
        description='The outer distance between the two ends.',
    ),
    'wholegenome_standard_dev': NextflowParameter(
        type=typing.Optional[int],
        default=50,
        section_title=None,
        description='The standard deviation.',
    ),
    'wholegenome_n_reads': NextflowParameter(
        type=typing.Optional[int],
        default=1000000,
        section_title=None,
        description='The number of read pairs.',
    ),
    'wholegenome_r1_length': NextflowParameter(
        type=typing.Optional[int],
        default=70,
        section_title=None,
        description='The length of the first reads.',
    ),
    'wholegenome_r2_length': NextflowParameter(
        type=typing.Optional[int],
        default=70,
        section_title=None,
        description='The length of the second reads.',
    ),
    'wholegenome_mutation_rate': NextflowParameter(
        type=typing.Optional[float],
        default=0.001,
        section_title=None,
        description='The rate of mutations.',
    ),
    'wholegenome_indel_fraction': NextflowParameter(
        type=typing.Optional[float],
        default=0.15,
        section_title=None,
        description='The fraction of indels.',
    ),
    'wholegenome_indel_extended': NextflowParameter(
        type=typing.Optional[float],
        default=0.3,
        section_title=None,
        description='The probability that an indel is extended.',
    ),
    'genome': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title='Reference genome options',
        description='Name of iGenomes reference.',
    ),
    'fasta': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Path to reference FASTA file.',
    ),
    'ncbidownload_accessions': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Path to text file containing accession ids (one accession per row).',
    ),
    'ncbidownload_taxids': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Path to text file containing taxids (one taxid per row).',
    ),
    'ncbidownload_group': NextflowParameter(
        type=typing.Optional[str],
        default='all',
        section_title=None,
        description="The NCBI taxonomic groups to download. Options include 'all', 'archaea', 'bacteria', 'fungi', 'invertebrate', 'metagenomes', 'plant', 'protozoa', 'vertebrate_mammalian', 'vertebrate_other', and 'viral'. A comma-separated list is also valid (e.g., 'bacteria,viral').",
    ),
    'ncbidownload_section': NextflowParameter(
        type=typing.Optional[str],
        default='refseq',
        section_title=None,
        description="The NCBI section to download. 'refseq' or 'genbank'.",
    ),
    'multiqc_methods_description': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title='Generic options',
        description='Custom MultiQC yaml file containing HTML including a methods description.',
    ),
}

