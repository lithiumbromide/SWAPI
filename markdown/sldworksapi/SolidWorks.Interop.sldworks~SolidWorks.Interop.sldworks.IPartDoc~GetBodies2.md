---
title: "GetBodies2 Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "GetBodies2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetBodies2.html"
---

# GetBodies2 Method (IPartDoc)

Gets the bodies in this part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBodies2( _
   ByVal BodyType As System.Integer, _
   ByVal BVisibleOnly As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim BodyType As System.Integer
Dim BVisibleOnly As System.Boolean
Dim value As System.Object

value = instance.GetBodies2(BodyType, BVisibleOnly)
```

### C#

```csharp
System.object GetBodies2(
   System.int BodyType,
   System.bool BVisibleOnly
)
```

### C++/CLI

```cpp
System.Object^ GetBodies2(
   System.int BodyType,
   System.bool BVisibleOnly
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyType`: Type of body as defined in [swBodyType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyType_e.html)
- `BVisibleOnly`: True gets only the visible bodies, false gets all of the bodies in the part

### Return Value

Array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [PartDoc::GetBodies2](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~GetBodies2.html).

## Examples

[Get Bodies (C++)](Get_Bodies_Example_CPlusPlus_COM.htm)
[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)
[Set Body for View (C#)](Set_Body_for_View_Example_CSharp.htm)
[Set Body for Part (VB.NET)](Set_Body_for_View_Example_VBNET.htm)
[Set Body for Part (VBA)](Set_Body_for_View_Example_VB.htm)

## Remarks

This method:

- Only supports solid and sheet (surface) body types.
- May vary the order in which bodies are returned.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IComponent2::GetBodies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBodies2.html)
[IBodyFolder::GetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetBodies.html)
[IBodyFolder::IGetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~IGetBodies.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
