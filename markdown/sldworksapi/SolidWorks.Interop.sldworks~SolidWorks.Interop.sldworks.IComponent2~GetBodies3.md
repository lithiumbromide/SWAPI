---
title: "GetBodies3 Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetBodies3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBodies3.html"
---

# GetBodies3 Method (IComponent2)

Gets the bodies in this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBodies3( _
   ByVal BodyType As System.Integer, _
   ByRef BodiesInfo As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim BodyType As System.Integer
Dim BodiesInfo As System.Object
Dim value As System.Object

value = instance.GetBodies3(BodyType, BodiesInfo)
```

### C#

```csharp
System.object GetBodies3(
   System.int BodyType,
   out System.object BodiesInfo
)
```

### C++/CLI

```cpp
System.Object^ GetBodies3(
   System.int BodyType,
   [Out] System.Object^ BodiesInfo
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyType`: Type of body as defined by [swBodyType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyType_e.html)
- `BodiesInfo`: Array of information about the returned bodies as defined in [swBodyInfo_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyInfo_e.html)

### Return Value

Array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) in the component

## VBA Syntax

See [Component2::GetBodies3](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetBodies3.html).

## Examples

Also see the [IView::GetVisibleDrawingComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleDrawingComponents.html) examples.

## Examples

[Get Bodies in Components (C#)](Get_Bodies_in_Components_Example_CSharp.htm)
[Get Bodies in Components (VB.NET)](Get_Bodies_in_Components_Example_VBNET.htm)
[Get Bodies in Components (VBA)](Get_Bodies_in_Components_Example_VB.htm)
[Get Bodies in Components (C++)](Get_Bodies_in_Components_Example_CPlusPlus_COM.htm)

## Remarks

This method:

- Only supports solid and surface bodies and part components,

- May vary the order in which bodies are returned,

- Supports lightweight components (the now obsolete IComponent2::GetBodies does not),

- and -

- Returns an array in BodiesInfo containing information about bodies that indicates whether they are normal or user bodies. User bodies are original component bodies that have been modified in an assembly (e.g., a normal component body is cut in the assembly, resulting in two user component bodies). User bodies are not created for surface bodies.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::EnumBodies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~EnumBodies2.html)
[IComponent2::GetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBody.html)
[IComponent2::IGetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetBody.html)
[IPartDoc::GetBodies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetBodies2.html)
[IBody2::IsSheetMetal Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsSheetMetal.html)

## Availability

SOLIDWORKS 2009 SP4, Revision Number 17.4
