# Conan Papi Recipe

## Upload Instructions

```
conan create . Papi/stable
conan upload Papi:5.7.0@Papi/stable -r bintray_repo
```

## Add Bintray Repository

```
conan remote add bintray_repo https://api.bintray.com/conan/antoinewaugh/Papi
```
