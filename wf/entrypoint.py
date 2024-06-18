from dataclasses import dataclass
from enum import Enum
import os
import subprocess
import requests
import shutil
from pathlib import Path
import typing
import typing_extensions

from latch.resources.workflow import workflow
from latch.resources.tasks import nextflow_runtime_task, custom_task
from latch.types.file import LatchFile
from latch.types.directory import LatchDir, LatchOutputDir
from latch.ldata.path import LPath
from latch_cli.nextflow.workflow import get_flag
from latch_cli.nextflow.utils import _get_execution_name
from latch_cli.utils import urljoins
from latch.types import metadata
from flytekit.core.annotation import FlyteAnnotation

from latch_cli.services.register.utils import import_module_by_path

meta = Path("latch_metadata") / "__init__.py"
import_module_by_path(meta)
import latch_metadata

@custom_task(cpu=0.25, memory=0.5, storage_gib=1)
def initialize() -> str:
    token = os.environ.get("FLYTE_INTERNAL_EXECUTION_ID")
    if token is None:
        raise RuntimeError("failed to get execution token")

    headers = {"Authorization": f"Latch-Execution-Token {token}"}

    print("Provisioning shared storage volume... ", end="")
    resp = requests.post(
        "http://nf-dispatcher-service.flyte.svc.cluster.local/provision-storage",
        headers=headers,
        json={
            "storage_gib": 100,
        }
    )
    resp.raise_for_status()
    print("Done.")

    return resp.json()["name"]






@nextflow_runtime_task(cpu=4, memory=8, storage_gib=100)
def nextflow_runtime(pvc_name: str, input: LatchFile, outdir: typing_extensions.Annotated[LatchDir, FlyteAnnotation({'output': True})], email: typing.Optional[str], multiqc_title: typing.Optional[str], amplicon: typing.Optional[bool], target_capture: typing.Optional[bool], metagenome: typing.Optional[bool], wholegenome: typing.Optional[bool], probe_file: typing.Optional[LatchFile], target_capture_tmedian: typing.Optional[int], target_capture_tshape: typing.Optional[float], metagenome_abundance_file: typing.Optional[LatchFile], metagenome_coverage: typing.Optional[str], metagenome_coverage_file: typing.Optional[LatchFile], metagenome_gc_bias: typing.Optional[bool], genome: typing.Optional[str], fasta: typing.Optional[LatchFile], ncbidownload_accessions: typing.Optional[LatchFile], ncbidownload_taxids: typing.Optional[LatchFile], multiqc_methods_description: typing.Optional[str], amplicon_fw_primer: typing.Optional[str], amplicon_rv_primer: typing.Optional[str], amplicon_read_count: typing.Optional[int], amplicon_read_length: typing.Optional[int], amplicon_seq_system: typing.Optional[str], amplicon_crabs_ispcr_error: typing.Optional[float], probe_ref_name: typing.Optional[str], target_capture_mode: typing.Optional[str], target_capture_fmedian: typing.Optional[int], target_capture_fshape: typing.Optional[float], target_capture_smedian: typing.Optional[int], target_capture_sshape: typing.Optional[float], target_capture_num: typing.Optional[int], target_capture_illen: typing.Optional[int], target_capture_pblen: typing.Optional[int], target_capture_ilmode: typing.Optional[str], metagenome_abundance: typing.Optional[str], metagenome_input_format: typing.Optional[str], metagenome_n_reads: typing.Optional[str], metagenome_mode: typing.Optional[str], metagenome_model: typing.Optional[str], wholegenome_error_rate: typing.Optional[float], wholegenome_outer_dist: typing.Optional[int], wholegenome_standard_dev: typing.Optional[int], wholegenome_n_reads: typing.Optional[int], wholegenome_r1_length: typing.Optional[int], wholegenome_r2_length: typing.Optional[int], wholegenome_mutation_rate: typing.Optional[float], wholegenome_indel_fraction: typing.Optional[float], wholegenome_indel_extended: typing.Optional[float], ncbidownload_group: typing.Optional[str], ncbidownload_section: typing.Optional[str]) -> None:
    try:
        shared_dir = Path("/nf-workdir")



        ignore_list = [
            "latch",
            ".latch",
            "nextflow",
            ".nextflow",
            "work",
            "results",
            "miniconda",
            "anaconda3",
            "mambaforge",
        ]

        shutil.copytree(
            Path("/root"),
            shared_dir,
            ignore=lambda src, names: ignore_list,
            ignore_dangling_symlinks=True,
            dirs_exist_ok=True,
        )

        cmd = [
            "/root/nextflow",
            "run",
            str(shared_dir / "main.nf"),
            "-work-dir",
            str(shared_dir),
            "-profile",
            "docker",
            "-c",
            "latch.config",
                *get_flag('input', input),
                *get_flag('outdir', outdir),
                *get_flag('email', email),
                *get_flag('multiqc_title', multiqc_title),
                *get_flag('amplicon', amplicon),
                *get_flag('target_capture', target_capture),
                *get_flag('metagenome', metagenome),
                *get_flag('wholegenome', wholegenome),
                *get_flag('amplicon_fw_primer', amplicon_fw_primer),
                *get_flag('amplicon_rv_primer', amplicon_rv_primer),
                *get_flag('amplicon_read_count', amplicon_read_count),
                *get_flag('amplicon_read_length', amplicon_read_length),
                *get_flag('amplicon_seq_system', amplicon_seq_system),
                *get_flag('amplicon_crabs_ispcr_error', amplicon_crabs_ispcr_error),
                *get_flag('probe_file', probe_file),
                *get_flag('probe_ref_name', probe_ref_name),
                *get_flag('target_capture_mode', target_capture_mode),
                *get_flag('target_capture_fmedian', target_capture_fmedian),
                *get_flag('target_capture_fshape', target_capture_fshape),
                *get_flag('target_capture_smedian', target_capture_smedian),
                *get_flag('target_capture_sshape', target_capture_sshape),
                *get_flag('target_capture_tmedian', target_capture_tmedian),
                *get_flag('target_capture_tshape', target_capture_tshape),
                *get_flag('target_capture_num', target_capture_num),
                *get_flag('target_capture_illen', target_capture_illen),
                *get_flag('target_capture_pblen', target_capture_pblen),
                *get_flag('target_capture_ilmode', target_capture_ilmode),
                *get_flag('metagenome_abundance', metagenome_abundance),
                *get_flag('metagenome_abundance_file', metagenome_abundance_file),
                *get_flag('metagenome_coverage', metagenome_coverage),
                *get_flag('metagenome_coverage_file', metagenome_coverage_file),
                *get_flag('metagenome_input_format', metagenome_input_format),
                *get_flag('metagenome_n_reads', metagenome_n_reads),
                *get_flag('metagenome_mode', metagenome_mode),
                *get_flag('metagenome_model', metagenome_model),
                *get_flag('metagenome_gc_bias', metagenome_gc_bias),
                *get_flag('wholegenome_error_rate', wholegenome_error_rate),
                *get_flag('wholegenome_outer_dist', wholegenome_outer_dist),
                *get_flag('wholegenome_standard_dev', wholegenome_standard_dev),
                *get_flag('wholegenome_n_reads', wholegenome_n_reads),
                *get_flag('wholegenome_r1_length', wholegenome_r1_length),
                *get_flag('wholegenome_r2_length', wholegenome_r2_length),
                *get_flag('wholegenome_mutation_rate', wholegenome_mutation_rate),
                *get_flag('wholegenome_indel_fraction', wholegenome_indel_fraction),
                *get_flag('wholegenome_indel_extended', wholegenome_indel_extended),
                *get_flag('genome', genome),
                *get_flag('fasta', fasta),
                *get_flag('ncbidownload_accessions', ncbidownload_accessions),
                *get_flag('ncbidownload_taxids', ncbidownload_taxids),
                *get_flag('ncbidownload_group', ncbidownload_group),
                *get_flag('ncbidownload_section', ncbidownload_section),
                *get_flag('multiqc_methods_description', multiqc_methods_description)
        ]

        print("Launching Nextflow Runtime")
        print(' '.join(cmd))
        print(flush=True)

        env = {
            **os.environ,
            "NXF_HOME": "/root/.nextflow",
            "NXF_OPTS": "-Xms2048M -Xmx8G -XX:ActiveProcessorCount=4",
            "K8S_STORAGE_CLAIM_NAME": pvc_name,
            "NXF_DISABLE_CHECK_LATEST": "true",
        }
        subprocess.run(
            cmd,
            env=env,
            check=True,
            cwd=str(shared_dir),
        )
    finally:
        print()

        nextflow_log = shared_dir / ".nextflow.log"
        if nextflow_log.exists():
            name = _get_execution_name()
            if name is None:
                print("Skipping logs upload, failed to get execution name")
            else:
                remote = LPath(urljoins("latch:///your_log_dir/nf_nf_core_readsimulator", name, "nextflow.log"))
                print(f"Uploading .nextflow.log to {remote.path}")
                remote.upload_from(nextflow_log)



@workflow(metadata._nextflow_metadata)
def nf_nf_core_readsimulator(input: LatchFile, outdir: typing_extensions.Annotated[LatchDir, FlyteAnnotation({'output': True})], email: typing.Optional[str], multiqc_title: typing.Optional[str], amplicon: typing.Optional[bool], target_capture: typing.Optional[bool], metagenome: typing.Optional[bool], wholegenome: typing.Optional[bool], probe_file: typing.Optional[LatchFile], target_capture_tmedian: typing.Optional[int], target_capture_tshape: typing.Optional[float], metagenome_abundance_file: typing.Optional[LatchFile], metagenome_coverage: typing.Optional[str], metagenome_coverage_file: typing.Optional[LatchFile], metagenome_gc_bias: typing.Optional[bool], genome: typing.Optional[str], fasta: typing.Optional[LatchFile], ncbidownload_accessions: typing.Optional[LatchFile], ncbidownload_taxids: typing.Optional[LatchFile], multiqc_methods_description: typing.Optional[str], amplicon_fw_primer: typing.Optional[str] = 'GTCGGTAAAACTCGTGCCAGC', amplicon_rv_primer: typing.Optional[str] = 'CATAGTGGGGTATCTAATCCCAGTTTG', amplicon_read_count: typing.Optional[int] = 500, amplicon_read_length: typing.Optional[int] = 130, amplicon_seq_system: typing.Optional[str] = 'HS25', amplicon_crabs_ispcr_error: typing.Optional[float] = 4.5, probe_ref_name: typing.Optional[str] = 'Tetrapods-UCE-5Kv1', target_capture_mode: typing.Optional[str] = 'illumina', target_capture_fmedian: typing.Optional[int] = 500, target_capture_fshape: typing.Optional[float] = 6, target_capture_smedian: typing.Optional[int] = 1300, target_capture_sshape: typing.Optional[float] = 6, target_capture_num: typing.Optional[int] = 500000, target_capture_illen: typing.Optional[int] = 150, target_capture_pblen: typing.Optional[int] = 30000, target_capture_ilmode: typing.Optional[str] = 'pe', metagenome_abundance: typing.Optional[str] = 'lognormal', metagenome_input_format: typing.Optional[str] = 'genomes', metagenome_n_reads: typing.Optional[str] = '1M', metagenome_mode: typing.Optional[str] = 'kde', metagenome_model: typing.Optional[str] = 'MiSeq', wholegenome_error_rate: typing.Optional[float] = 0.02, wholegenome_outer_dist: typing.Optional[int] = 500, wholegenome_standard_dev: typing.Optional[int] = 50, wholegenome_n_reads: typing.Optional[int] = 1000000, wholegenome_r1_length: typing.Optional[int] = 70, wholegenome_r2_length: typing.Optional[int] = 70, wholegenome_mutation_rate: typing.Optional[float] = 0.001, wholegenome_indel_fraction: typing.Optional[float] = 0.15, wholegenome_indel_extended: typing.Optional[float] = 0.3, ncbidownload_group: typing.Optional[str] = 'all', ncbidownload_section: typing.Optional[str] = 'refseq') -> None:
    """
    nf-core/readsimulator

    Sample Description
    """

    pvc_name: str = initialize()
    nextflow_runtime(pvc_name=pvc_name, input=input, outdir=outdir, email=email, multiqc_title=multiqc_title, amplicon=amplicon, target_capture=target_capture, metagenome=metagenome, wholegenome=wholegenome, amplicon_fw_primer=amplicon_fw_primer, amplicon_rv_primer=amplicon_rv_primer, amplicon_read_count=amplicon_read_count, amplicon_read_length=amplicon_read_length, amplicon_seq_system=amplicon_seq_system, amplicon_crabs_ispcr_error=amplicon_crabs_ispcr_error, probe_file=probe_file, probe_ref_name=probe_ref_name, target_capture_mode=target_capture_mode, target_capture_fmedian=target_capture_fmedian, target_capture_fshape=target_capture_fshape, target_capture_smedian=target_capture_smedian, target_capture_sshape=target_capture_sshape, target_capture_tmedian=target_capture_tmedian, target_capture_tshape=target_capture_tshape, target_capture_num=target_capture_num, target_capture_illen=target_capture_illen, target_capture_pblen=target_capture_pblen, target_capture_ilmode=target_capture_ilmode, metagenome_abundance=metagenome_abundance, metagenome_abundance_file=metagenome_abundance_file, metagenome_coverage=metagenome_coverage, metagenome_coverage_file=metagenome_coverage_file, metagenome_input_format=metagenome_input_format, metagenome_n_reads=metagenome_n_reads, metagenome_mode=metagenome_mode, metagenome_model=metagenome_model, metagenome_gc_bias=metagenome_gc_bias, wholegenome_error_rate=wholegenome_error_rate, wholegenome_outer_dist=wholegenome_outer_dist, wholegenome_standard_dev=wholegenome_standard_dev, wholegenome_n_reads=wholegenome_n_reads, wholegenome_r1_length=wholegenome_r1_length, wholegenome_r2_length=wholegenome_r2_length, wholegenome_mutation_rate=wholegenome_mutation_rate, wholegenome_indel_fraction=wholegenome_indel_fraction, wholegenome_indel_extended=wholegenome_indel_extended, genome=genome, fasta=fasta, ncbidownload_accessions=ncbidownload_accessions, ncbidownload_taxids=ncbidownload_taxids, ncbidownload_group=ncbidownload_group, ncbidownload_section=ncbidownload_section, multiqc_methods_description=multiqc_methods_description)

