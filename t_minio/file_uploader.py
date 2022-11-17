# *_*coding:utf-8 *_*
# @Author : Reggie
# @Time : 2022/11/2 10:09
import os

from minio import Minio
from minio.error import S3Error


def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        "192.168.1.149:9000",
        access_key="wtt",
        secret_key="wangtong123.",
        secure=False
    )
    bucket_name = "image"
    # Make 'asiatrip' bucket if not exist.
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
    else:
        print(f"Bucket '{bucket_name}' already exists")

    data = client.get_bucket_policy(bucket_name)
    print(f"Bucket '{bucket_name}' {data}")

    object_name = "test.jpg"
    file_path = "../t_wordcloud/Alice.png"
    # Upload '/home/user/Photos/asiaphotos.zip' as object name
    # 'asiaphotos-2015.zip' to bucket 'asiatrip'.

    result = client.fput_object(
        bucket_name=bucket_name,
        object_name=object_name,
        file_path=file_path,
    )
    print(
        f"'{file_path}' is successfully uploaded as "
        f"object '{object_name}' to bucket '{bucket_name}'."
    )
    print(result.version_id)
    object_name = "v2-bda6364fa5616eaf82c1b3ee6683a2f0_r.jpeg"
    file_path = r"C:\Users\wt\Pictures\v2-bda6364fa5616eaf82c1b3ee6683a2f0_r.jpeg"
    result = client.fput_object(
        bucket_name=bucket_name,
        object_name=object_name,
        file_path=file_path,
    )
    print(
        f"'{file_path}' is successfully uploaded as "
        f"object '{object_name}' to bucket '{bucket_name}'."
    )
    print(result.version_id)
    object_name = "bda6364fa5616eaf82c1b3ee6683a2f0_r.jpeg"
    file_path = r"C:\Users\wt\Pictures\v2-bda6364fa5616eaf82c1b3ee6683a2f0_r.jpeg"
    file_size = os.stat(file_path).st_size
    with open(file_path, 'rb') as file_data:
        client.put_object(
            bucket_name=bucket_name,
            object_name=object_name,
            data=file_data,
            length=file_size,
        )
    print(
        f"'{file_path}' is successfully uploaded as "
        f"object '{object_name}' to bucket '{bucket_name}'."
    )

    # # Get data of an object.
    # try:
    #     response = client.get_object(bucket_name, object_name)
    #     # Read data from response.
    #     with open(object_name, 'wb') as f:
    #         f.write(response.data)
    # finally:
    #     response.close()
    #     response.release_conn()

    # Get object information.
    result = client.stat_object(bucket_name, object_name)
    print(
        "last-modified: {0}, size: {1}".format(
            result.last_modified, result.size,
        ),
    )
    # Get object information.
    result = client.get_presigned_url("GET", bucket_name, object_name)
    print(result)


if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)
