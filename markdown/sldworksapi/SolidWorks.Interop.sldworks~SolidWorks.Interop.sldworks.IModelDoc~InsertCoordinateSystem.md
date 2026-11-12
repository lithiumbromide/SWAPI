---
title: "InsertCoordinateSystem Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertCoordinateSystem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertCoordinateSystem.html"
---

# InsertCoordinateSystem Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertCoordinateSystem](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertCoordinateSystem.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertCoordinateSystem( _
   ByVal XFlippedIn As System.Boolean, _
   ByVal YFlippedIn As System.Boolean, _
   ByVal ZFlippedIn As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim XFlippedIn As System.Boolean
Dim YFlippedIn As System.Boolean
Dim ZFlippedIn As System.Boolean
Dim value As System.Boolean

value = instance.InsertCoordinateSystem(XFlippedIn, YFlippedIn, ZFlippedIn)
```

### C#

```csharp
System.bool InsertCoordinateSystem(
   System.bool XFlippedIn,
   System.bool YFlippedIn,
   System.bool ZFlippedIn
)
```

### C++/CLI

```cpp
System.bool InsertCoordinateSystem(
   System.bool XFlippedIn,
   System.bool YFlippedIn,
   System.bool ZFlippedIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XFlippedIn`:
- `YFlippedIn`:
- `ZFlippedIn`:

## VBA Syntax

See [ModelDoc::InsertCoordinateSystem](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertCoordinateSystem.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
