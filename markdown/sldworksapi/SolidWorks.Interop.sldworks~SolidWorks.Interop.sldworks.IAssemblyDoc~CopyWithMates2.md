---
title: "CopyWithMates2 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "CopyWithMates2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CopyWithMates2.html"
---

# CopyWithMates2 Method (IAssemblyDoc)

Copies one or more components with mates in this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function CopyWithMates2( _
   ByVal ComponentsToCopy As System.Object, _
   ByVal Repeat As System.Object, _
   ByVal NewEnityToMateTo As System.Object, _
   ByVal Values As System.Object, _
   ByVal FlipAlignment As System.Object, _
   ByVal FlipDimension As System.Object, _
   ByVal LockRotation As System.Object, _
   ByVal Orientation As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim ComponentsToCopy As System.Object
Dim Repeat As System.Object
Dim NewEnityToMateTo As System.Object
Dim Values As System.Object
Dim FlipAlignment As System.Object
Dim FlipDimension As System.Object
Dim LockRotation As System.Object
Dim Orientation As System.Object
Dim value As System.Boolean

value = instance.CopyWithMates2(ComponentsToCopy, Repeat, NewEnityToMateTo, Values, FlipAlignment, FlipDimension, LockRotation, Orientation)
```

### C#

```csharp
System.bool CopyWithMates2(
   System.object ComponentsToCopy,
   System.object Repeat,
   System.object NewEnityToMateTo,
   System.object Values,
   System.object FlipAlignment,
   System.object FlipDimension,
   System.object LockRotation,
   System.object Orientation
)
```

### C++/CLI

```cpp
System.bool CopyWithMates2(
   System.Object^ ComponentsToCopy,
   System.Object^ Repeat,
   System.Object^ NewEnityToMateTo,
   System.Object^ Values,
   System.Object^ FlipAlignment,
   System.Object^ FlipDimension,
   System.Object^ LockRotation,
   System.Object^ Orientation
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ComponentsToCopy`: Array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html) to copy
- `Repeat`: Array of boolean values; each value indicates whether to use the existing mate reference for the corresponding component to copy; if true, copies the existing mate reference; if false, uses the corresponding entry in the NewEntityToMateTo array for the new mate reference
- `NewEnityToMateTo`: Array of new mate references that map to the Repeat array; if an entry in the Repeat array is false, then the corresponding entry in this array is the new entity with which to mate the component to copy
- `Values`: Array of distance or angle values for the mate references; specify distance in meters and angle in radians; valid for distance, angle, and profile center mates only
- `FlipAlignment`: Array of booleans that map to the NewEntityToMateTo array; each value indicates the corresponding mate's alignment; true to flip alignment, false to not
- `FlipDimension`: Array of booleans that map to the Values array; each value indicates the corresponding mate's distance; true for a positive distance dimension, false for a negative distance dimension; valid for distance, angle, and profile center mates only
- `LockRotation`: Array of booleans that map to the NewEntityToMateTo array; true to prevent the components from rotating, false to allow the components to rotate; valid for concentric and profile center mates only
- `Orientation`: Array of longs or integers that map to the Values array; each long or integer indicates the number of clicks in the user interface with which to orient the mate; a positive value indicates to orient the mate clockwise, a negative value indicates to orient the mate counterclockwise; valid for profile center mates only

### Return Value

True if calling this method succeeded, false if it failed

## VBA Syntax

See [AssemblyDoc::CopyWithMates2](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~CopyWithMates2.html).

## Examples

[Copy Component With Profile Center Mate (C#)](Copy_Component_With_Profile_Center_Mate_Example_CSharp.htm)
[Copy Component With Profile Center Mate (VB.NET)](Copy_Component_With_Profile_Center_Mate_Example_VBNET.htm)
[Copy Component With Profile Center Mate (VBA)](Copy_Component_With_Profile_Center_Mate_Example_VB.htm)

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::AddComponent5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponent5.html)
[IAssemblyDoc::AddMate5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddMate5.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
