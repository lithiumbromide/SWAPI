---
title: "GetLightSourceIdFromName Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GetLightSourceIdFromName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetLightSourceIdFromName.html"
---

# GetLightSourceIdFromName Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GetLightSourceIdFromName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetLightSourceIdFromName.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLightSourceIdFromName( _
   ByVal LightName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim LightName As System.String
Dim value As System.Integer

value = instance.GetLightSourceIdFromName(LightName)
```

### C#

```csharp
System.int GetLightSourceIdFromName(
   System.string LightName
)
```

### C++/CLI

```cpp
System.int GetLightSourceIdFromName(
   System.String^ LightName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LightName`:

## VBA Syntax

See [ModelDoc::GetLightSourceIdFromName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GetLightSourceIdFromName.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
