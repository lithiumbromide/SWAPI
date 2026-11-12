---
title: "InsertRouteLine Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "InsertRouteLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~InsertRouteLine.html"
---

# InsertRouteLine Method (ISketch)

Inserts a route line in an explode line sketch or a 3D sketch to indicate component relationships.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertRouteLine( _
   ByVal ItemsToConnect As System.Object, _
   ByVal Reverse As System.Object, _
   ByVal AlternatePath As System.Object, _
   ByVal AlongXYZ As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim ItemsToConnect As System.Object
Dim Reverse As System.Object
Dim AlternatePath As System.Object
Dim AlongXYZ As System.Object
Dim value As System.Boolean

value = instance.InsertRouteLine(ItemsToConnect, Reverse, AlternatePath, AlongXYZ)
```

### C#

```csharp
System.bool InsertRouteLine(
   System.object ItemsToConnect,
   System.object Reverse,
   System.object AlternatePath,
   System.object AlongXYZ
)
```

### C++/CLI

```cpp
System.bool InsertRouteLine(
   System.Object^ ItemsToConnect,
   System.Object^ Reverse,
   System.Object^ AlternatePath,
   System.Object^ AlongXYZ
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ItemsToConnect`: Array of faces, edges, and vertices to which to connect the route line
- `Reverse`: Array of Booleans indicating whether to reverse the route line at the corresponding item to connect; true to reverse the direction of the route line, false to not
- `AlternatePath`: Array of Booleans indicating whether to display an alternate path at the corresponding item to connect; true to display another possible path for the route line, false to not
- `AlongXYZ`: Array of Booleans indicating whether to create a path parallel to the X, Y, and Z directions from the corresponding item to connect; true to use the X, Y, and Z directions, false to use the shortest route

### Return Value

True if a route line is inserted, false if not

## VBA Syntax

See [Sketch::InsertRouteLine](ms-its:sldworksapivb6.chm::/sldworks~Sketch~InsertRouteLine.html).

## Examples

[Insert Explode Line Sketch and Route Line (VB.NET)](Insert_Exploded_Line_Sketch_and_Route_Line_Example_VBNET.htm)
[Insert Explode Line Sketch and Route Line (VBA)](Insert_Exploded_Line_Sketch_and_Route_Line_Example_VB.htm)
[Insert Explode Line Sketch and Route Line (C#)](Insert_Exploded_Line_Sketch_and_Route_Line_Example_CSharp.htm)

## Remarks

You insert a route line in an [explode line sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~InsertExplodeLineSketch.html).

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[IAssemblyDoc::AutoExplode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoExplode.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
