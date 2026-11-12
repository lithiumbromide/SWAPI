---
title: "IGetMassProperties Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IGetMassProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetMassProperties.html"
---

# IGetMassProperties Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::GetMassProperties2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetMassProperties2.html) and [ISldWorks::IGetMassProperties2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IGetMassProperties2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMassProperties( _
   ByVal FilePathName As System.String, _
   ByVal ConfigurationName As System.String, _
   ByRef MPropsData As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FilePathName As System.String
Dim ConfigurationName As System.String
Dim MPropsData As System.Double
Dim value As System.Boolean

value = instance.IGetMassProperties(FilePathName, ConfigurationName, MPropsData)
```

### C#

```csharp
System.bool IGetMassProperties(
   System.string FilePathName,
   System.string ConfigurationName,
   ref System.double MPropsData
)
```

### C++/CLI

```cpp
System.bool IGetMassProperties(
   System.String^ FilePathName,
   System.String^ ConfigurationName,
   System.double% MPropsData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilePathName`:
- `ConfigurationName`:
- `MPropsData`:

## VBA Syntax

See [SldWorks::IGetMassProperties](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IGetMassProperties.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
