---
title: "IAddOrEditConfiguration Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IAddOrEditConfiguration"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddOrEditConfiguration.html"
---

# IAddOrEditConfiguration Method (IModelDoc2)

Obsolete. Superseded by [IConfiguraiton::GetParameters](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetParameters.html), [IConfiguration::IGetParameters](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~IGetParameters.html), [IConfiguration::ISetParameters](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~ISetParameters.html), and [IConfiguration::SetParameters](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~SetParameters.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddOrEditConfiguration( _
   ByVal ConfigName As System.String, _
   ByVal ParamCount As System.Integer, _
   ByRef ParamNames As System.String, _
   ByRef ParamValues As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim ConfigName As System.String
Dim ParamCount As System.Integer
Dim ParamNames As System.String
Dim ParamValues As System.String
Dim value As System.Integer

value = instance.IAddOrEditConfiguration(ConfigName, ParamCount, ParamNames, ParamValues)
```

### C#

```csharp
System.int IAddOrEditConfiguration(
   System.string ConfigName,
   System.int ParamCount,
   ref System.string ParamNames,
   ref System.string ParamValues
)
```

### C++/CLI

```cpp
System.int IAddOrEditConfiguration(
   System.String^ ConfigName,
   System.int ParamCount,
   System.String^% ParamNames,
   System.String^% ParamValues
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigName`:
- `ParamCount`:
- `ParamNames`:
- `ParamValues`:

## VBA Syntax

See [ModelDoc2::IAddOrEditConfiguration](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IAddOrEditConfiguration.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
