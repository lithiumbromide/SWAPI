---
title: "GetLightSourceExtProperty Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GetLightSourceExtProperty"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetLightSourceExtProperty.html"
---

# GetLightSourceExtProperty Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GetLightSourceExtProperty](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetLightSourceExtProperty.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLightSourceExtProperty( _
   ByVal ID As System.Integer, _
   ByVal PropertyId As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim ID As System.Integer
Dim PropertyId As System.Integer
Dim value As System.Object

value = instance.GetLightSourceExtProperty(ID, PropertyId)
```

### C#

```csharp
System.object GetLightSourceExtProperty(
   System.int ID,
   System.int PropertyId
)
```

### C++/CLI

```cpp
System.Object^ GetLightSourceExtProperty(
   System.int ID,
   System.int PropertyId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`:
- `PropertyId`:

## VBA Syntax

See [ModelDoc::GetLightSourceExtProperty](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GetLightSourceExtProperty.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
