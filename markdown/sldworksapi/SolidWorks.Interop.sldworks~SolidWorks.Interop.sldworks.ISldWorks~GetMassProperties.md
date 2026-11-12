---
title: "GetMassProperties Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetMassProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMassProperties.html"
---

# GetMassProperties Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::GetMassProperties2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetMassProperties2.html) and [ISldWorks::IGetMassProperties2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IGetMassProperties2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMassProperties( _
   ByVal FilePathName As System.String, _
   ByVal ConfigurationName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FilePathName As System.String
Dim ConfigurationName As System.String
Dim value As System.Object

value = instance.GetMassProperties(FilePathName, ConfigurationName)
```

### C#

```csharp
System.object GetMassProperties(
   System.string FilePathName,
   System.string ConfigurationName
)
```

### C++/CLI

```cpp
System.Object^ GetMassProperties(
   System.String^ FilePathName,
   System.String^ ConfigurationName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilePathName`:
- `ConfigurationName`:

## VBA Syntax

See [SldWorks::GetMassProperties](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetMassProperties.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
