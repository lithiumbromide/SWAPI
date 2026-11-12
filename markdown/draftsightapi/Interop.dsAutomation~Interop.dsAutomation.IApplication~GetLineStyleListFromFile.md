---
title: "GetLineStyleListFromFile Method (IApplication)"
project: ""
interface: "IApplication"
member: "GetLineStyleListFromFile"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~GetLineStyleListFromFile.html"
---

# GetLineStyleListFromFile Method (IApplication)

Gets the names of the simple [LineStyles](Interop.dsAutomation~Interop.dsAutomation.ILineStyle.html) and their descriptions contained in the specified LineStyle file.

## Syntax

### Visual Basic

```vb
Sub GetLineStyleListFromFile( _
   ByVal FileName As System.String, _
   ByRef NameStrArray As System.Object, _
   ByRef DescriptionStrArray As System.Object _
)
```

### C#

```csharp
void GetLineStyleListFromFile(
   System.string FileName,
   out System.object NameStrArray,
   out System.object DescriptionStrArray
)
```

### JScript

```
function GetLineStyleListFromFile(
   FileName : System.String,
   NameStrArray : System.Object,
   DescriptionStrArray : System.Object
);
```

### Managed Extensions for C++

```
void GetLineStyleListFromFile(
   System.string* FileName,
   [PARAMFLAG::Out] System.Object* NameStrArray,
   [PARAMFLAG::Out] System.Object* DescriptionStrArray
)
```

### C++/CLI

```cpp
void GetLineStyleListFromFile(
   System.String^ FileName,
   [Out] System.Object^ NameStrArray,
   [Out] System.Object^ DescriptionStrArray
)
```

### Parameters

- `FileName`: Path and file name of the file containing the names of the LineStyles and their descriptions (see **Remarks**)
- `NameStrArray`: Names of the LineStyles in FileName
- `DescriptionStrArray`: Descriptions of the LineStyles in FileName

## Remarks

Simple LineStyle definition files are stored in ASCII text files with **.lin** filename extensions.

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::CreateLineStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateLineStyle.html)

## Availability

DraftSight V1R4.0
