#!/bin/bash
__rpnpy_version=2.2.0-rc3
__rpnpy_x=x/
__rpnpy_basedir=/fs/ssm/eccc/mrd/rpn/MIG/ENV/d/rpnpy/${__rpnpy_x}${__rpnpy_version}
. ${__rpnpy_basedir}/bin/.env_setup.dot rpnpy ${__rpnpy_version##x/} all ${__rpnpy_basedir} ${__rpnpy_basedir}
unset __rpnpy_version __rpnpy_basedir __rpnpy_x
