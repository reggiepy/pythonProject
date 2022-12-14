# -*- coding: utf-8 -*-
# MinIO Python Library for Amazon S3 Compatible Cloud Storage,
# (C) 2022 MinIO, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from minio import Minio
from minio.credentials import CertificateIdentityProvider

# STS endpoint usually point to MinIO server.
sts_endpoint = "https://STS-HOST:STS-PORT/"

# client certificate file
cert_file = "/path/to/client.pem"

# client private key
key_file = "/path/to/client.key"

provider = CertificateIdentityProvider(
    sts_endpoint, cert_file=cert_file, key_file=key_file,
)

client = Minio("MINIO-HOST:MINIO-PORT", credentials=provider)

# Get information of an object.
stat = client.stat_object("my-bucket", "my-object")
print(stat)
