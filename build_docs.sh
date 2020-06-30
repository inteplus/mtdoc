#!/bin/bash

VERSION_YEAR=`date +'%Y'`
VERSION_MONTH=`date +'%m'`
VERSION_DAY=`date +'%d'`
VERSION_DATE=`date +'%Y%m%d'`
VERSION_HOUR=`date +'%H'`
VERSION_MINUTE=`date +'%M'`

SCRIPT_PATH="$( cd "$(dirname "$0")" ; pwd -P )"

# version.py
mkdir -p ${SCRIPT_PATH}/docs
echo "Updating ${SCRIPT_PATH}/docs/version.py..."
echo "VERSION_YEAR = ${VERSION_YEAR}"$'\r' > ${SCRIPT_PATH}/docs/version.py
echo "VERSION_MONTH = int('${VERSION_MONTH}')"$'\r' >> ${SCRIPT_PATH}/docs/version.py
echo "VERSION_DAY = int('${VERSION_DAY}')"$'\r' >> ${SCRIPT_PATH}/docs/version.py
echo "VERSION_HOUR = int('${VERSION_HOUR}')"$'\r' >> ${SCRIPT_PATH}/docs/version.py
echo "VERSION_MINUTE = int('${VERSION_MINUTE}')"$'\r\r' >> ${SCRIPT_PATH}/docs/version.py

echo "MAJOR_VERSION = ${VERSION_YEAR}"$'\r' >> ${SCRIPT_PATH}/docs/version.py
echo "MINOR_VERSION = '9${VERSION_MONTH}${VERSION_DAY}'"$'\r' >> ${SCRIPT_PATH}/docs/version.py
echo "PATCH_VERSION = '9${VERSION_HOUR}${VERSION_MINUTE}'"$'\r' >> ${SCRIPT_PATH}/docs/version.py
echo "version_date = '${VERSION_YEAR}/${VERSION_MONTH}/${VERSION_DAY} ${VERSION_HOUR}:${VERSION_MINUTE}'"$'\r' >> ${SCRIPT_PATH}/docs/version.py
echo "version = '{}.{}.{}'.format(MAJOR_VERSION, MINOR_VERSION, PATCH_VERSION)"$'\r' >> ${SCRIPT_PATH}/docs/version.py

git pull
git commit -am "auto-generated as of ${VERSION_YEAR}-${VERSION_MONTH}-${VERSION_DAY} ${VERSION_HOUR}:${VERSION_MINUTE}"
git push

cd docs
make html
cd ..

# s3cmd put --recursive --acl-public docs/_build/html/ s3:///e5251f96e0164a19b3cd12c7a0b3174a/wml.docs/
