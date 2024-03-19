from setuptools import find_packages, setup

setup(
    name="cityflowenv",
    version="0.0.0",
    description="A gym-like environment for CityFlow. Install CityFlow first and then install cityflowenv.",
    author="kearney",
    author_email="191615342@qq.com",
    requires=["numpy"],
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "cityflowenv": ["cityflow_data/*"],
    },
    license="apache 3.0",
)
