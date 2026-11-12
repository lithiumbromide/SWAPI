---
title: "GetSceneExtProperty Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GetSceneExtProperty"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetSceneExtProperty.html"
---

# GetSceneExtProperty Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GetSceneExtProperty](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetSceneExtProperty.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSceneExtProperty( _
   ByVal PropertyId As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim PropertyId As System.Integer
Dim value As System.Object

value = instance.GetSceneExtProperty(PropertyId)
```

### C#

```csharp
System.object GetSceneExtProperty(
   System.int PropertyId
)
```

### C++/CLI

```cpp
System.Object^ GetSceneExtProperty(
   System.int PropertyId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PropertyId`:

## VBA Syntax

See [ModelDoc::GetSceneExtProperty](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GetSceneExtProperty.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
