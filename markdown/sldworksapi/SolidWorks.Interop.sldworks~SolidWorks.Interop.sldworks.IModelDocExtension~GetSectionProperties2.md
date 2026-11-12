---
title: "GetSectionProperties2 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetSectionProperties2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSectionProperties2.html"
---

# GetSectionProperties2 Method (IModelDocExtension)

Gets the section properties for the following types of selected items:

- Planar model face in any document
- Face on a section plane
- Crosshatch section face in a section view in a drawing a sketch
- Sketch

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSectionProperties2( _
   ByVal Sections As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Sections As System.Object
Dim value As System.Object

value = instance.GetSectionProperties2(Sections)
```

### C#

```csharp
System.object GetSectionProperties2(
   System.object Sections
)
```

### C++/CLI

```cpp
System.Object^ GetSectionProperties2(
   System.Object^ Sections
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Sections`: Array of sections

### Return Value

Array of section properties for the selected items (see **Remarks**)

## VBA Syntax

See [ModelDocExtension::GetSectionProperties2](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetSectionProperties2.html).

## Examples

[Get Section Properties for Planar Faces (VBA)](Get_Section_Properties_Example2_VB.htm)

## Remarks

This method clears the selection set.

| If... | Then... |
| --- | --- |
| The user selected a set of either parallel planes or parallel faces | You can pass an empty sections array |
| The user selected any items and you pass a sections array | The properties of the user-selected items and the sections array are combined in the returned array |
| You pass a sections array and you do not want this array combined with the properties of any user-selected items | Clear any user-selected items |

The objects in the Sections parameter are added to the current selection set. If the objects are already in the current selection set, an error is generated; that is, status code will be equal to 1, which means invalid input.

The format of the returned array (retval) of size 24:

| retval[0] | status of request: 0 = success 1 = invalid input 2 = selected faces are not in the same or parallel planes 3 = unable to compute section properties |
| --- | --- |
| retval[1] | area |
| retval[2] | centroid x |
| retval[3] | centroid y |
| retval[4] | centroid z |
| retval[5] | moment of inertia XX |
| reval[6] | moment of inertia YY |
| retval[7] | moment of inertia ZZ |
| retval[8] | moment of inertia -XY |
| retval[9] | moment of inertia -ZX |
| retval[10] | moment of inertia -YZ |
| retval[11] | polar moment of inertia of an area at the centroid |
| retval[12] | angle between principal axis and part axis |
| retval[13] | principal moment of inertia of an area at the centroid, lx |
| retval[14] | principal moment of inertia of an area at the centroid, ly |
| retval[15] | direction vector X for principle axes (x component) |
| retval[16] | direction vector X for principle axes (y component) |
| retval[17] | direction vector X for principle axes (z component) |
| retval[18] | direction vector Y for principle axes (x component) |
| retval[19] | direction vector Y for principle axes (y component) |
| retval[20] | direction vector Y for principle axes (z component) |
| retval[21] | direction vector Z for principle axes (x component) |
| retval[22] | direction vector Z for principle axes (y component) |
| retval[23] | direction vector Z for principle axes (z component) |

This method returns metric units unless explicitly specified otherwise.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::IGetSectionProperties2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetSectionProperties2.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
