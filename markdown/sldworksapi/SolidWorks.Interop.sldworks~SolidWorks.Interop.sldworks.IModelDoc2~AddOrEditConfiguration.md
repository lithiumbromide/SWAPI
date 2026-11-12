---
title: "AddOrEditConfiguration Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "AddOrEditConfiguration"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddOrEditConfiguration.html"
---

# AddOrEditConfiguration Method (IModelDoc2)

Obsolete. Superseded by [IConfiguraiton::GetParameters](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetParameters.html), [IConfiguration::IGetParameters](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~IGetParameters.html), [IConfiguration::ISetParameters](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~ISetParameters.html), and [IConfiguration::SetParameters](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~SetParameters.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddOrEditConfiguration( _
   ByVal ConfigName As System.String, _
   ByVal Params As System.Object, _
   ByVal Values As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim ConfigName As System.String
Dim Params As System.Object
Dim Values As System.Object
Dim value As System.Integer

value = instance.AddOrEditConfiguration(ConfigName, Params, Values)
```

### C#

```csharp
System.int AddOrEditConfiguration(
   System.string ConfigName,
   System.object Params,
   System.object Values
)
```

### C++/CLI

```cpp
System.int AddOrEditConfiguration(
   System.String^ ConfigName,
   System.Object^ Params,
   System.Object^ Values
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigName`:
- `Params`:
- `Values`:

## VBA Syntax

See [ModelDoc2::AddOrEditConfiguration](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~AddOrEditConfiguration.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
