---
title: "Stretch Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "Stretch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Stretch.html"
---

# Stretch Method (IModelDocExtension)

Stretch the selected entities.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Stretch( _
   ByVal KeepRelations As System.Boolean, _
   ByVal BaseX As System.Double, _
   ByVal BaseY As System.Double, _
   ByVal DestX As System.Double, _
   ByVal DestY As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim KeepRelations As System.Boolean
Dim BaseX As System.Double
Dim BaseY As System.Double
Dim DestX As System.Double
Dim DestY As System.Double

instance.Stretch(KeepRelations, BaseX, BaseY, DestX, DestY)
```

### C#

```csharp
void Stretch(
   System.bool KeepRelations,
   System.double BaseX,
   System.double BaseY,
   System.double DestX,
   System.double DestY
)
```

### C++/CLI

```cpp
void Stretch(
   System.bool KeepRelations,
   System.double BaseX,
   System.double BaseY,
   System.double DestX,
   System.double DestY
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `KeepRelations`: True to keep the sketch relations intact, false to sever them
- `BaseX`: x coordinate of the base point
- `BaseY`: y coordinate of the base point
- `DestX`: x coordinate of the destination stretch
- `DestY`: y coordinate of the destination of the stretch

## VBA Syntax

See [ModelDocExtension::Stretch](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~Stretch.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
