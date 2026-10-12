---
title: "CreatePlaneAtOffset2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreatePlaneAtOffset2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreatePlaneAtOffset2.html"
---

# CreatePlaneAtOffset2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreatePlaneAtOffset2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreatePlaneAtOffset2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreatePlaneAtOffset2( _
   ByVal Val As System.Double, _
   ByVal FlipDir As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Val As System.Double
Dim FlipDir As System.Boolean
Dim value As System.Object

value = instance.CreatePlaneAtOffset2(Val, FlipDir)
```

### C#

```csharp
System.object CreatePlaneAtOffset2(
   System.double Val,
   System.bool FlipDir
)
```

### C++/CLI

```cpp
System.Object^ CreatePlaneAtOffset2(
   System.double Val,
   System.bool FlipDir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Val`:
- `FlipDir`:

## VBA Syntax

See [ModelDoc::CreatePlaneAtOffset2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreatePlaneAtOffset2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
