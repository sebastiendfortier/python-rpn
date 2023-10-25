#!/bin/bash
__rpnphy_version=x/2.2.0-rc2
__rpnpy_basedir=/fs/ssm/eccc/mrd/rpn/MIG/ENV/d/rpnpy/${__rpnphy_version}
${__rpnpy_basedir}/bin/.env_setup.dot rpnpy ${__rpnphy_version##x/} all ${__rpnpy_basedir} ${__rpnpy_basedir}
unset __rpnphy_version __rpnphy_basedir
