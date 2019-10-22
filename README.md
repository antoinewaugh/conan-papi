# Conan Papi Recipe

## Usage

### Add remote

```
conan remote add Papi https://api.bintray.com/conan/antoinewaugh/Papi
```

### Add dependency to conanfile.txt

```
//conanfile.txt

[requires]
Papi/5.7.0@Papi/stable

[generators]
cmake
```

----------------------


## Upload Instructions

```
conan create . Papi/stable
conan upload Papi:5.7.0@Papi/stable -r bintray_repo
```

## Add Bintray Repository

```
conan remote add bintray_repo https://api.bintray.com/conan/antoinewaugh/Papi
```
