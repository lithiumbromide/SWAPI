---
title: "AddOrdinateDimension Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "AddOrdinateDimension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddOrdinateDimension.html"
---

# AddOrdinateDimension Method (IDrawingDoc)

Obsolete. Superseded by [IModelDocExtension::AddOrdinateDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~AddOrdinateDimension.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddOrdinateDimension( _
   ByVal DimType As System.Integer, _
   ByVal LocX As System.Double, _
   ByVal LocY As System.Double, _
   ByVal LocZ As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim DimType As System.Integer
Dim LocX As System.Double
Dim LocY As System.Double
Dim LocZ As System.Double
Dim value As System.Boolean

value = instance.AddOrdinateDimension(DimType, LocX, LocY, LocZ)
```

### C#

```csharp
System.bool AddOrdinateDimension(
   System.int DimType,
   System.double LocX,
   System.double LocY,
   System.double LocZ
)
```

### C++/CLI

```cpp
System.bool AddOrdinateDimension(
   System.int DimType,
   System.double LocX,
   System.double LocY,
   System.double LocZ
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DimType`:
- `LocX`:
- `LocY`:
- `LocZ`:

## VBA Syntax

See [DrawingDoc::AddOrdinateDimension](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~AddOrdinateDimension.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
