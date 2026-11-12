---
title: "GetBendLineValues2 Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetBendLineValues2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBendLineValues2.html"
---

# GetBendLineValues2 Method (INote)

Gets the values of a bend line note.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBendLineValues2( _
   ByRef Up As System.Boolean, _
   ByRef Angle As System.Double, _
   ByRef Radius As System.Double, _
   ByRef Points As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim Up As System.Boolean
Dim Angle As System.Double
Dim Radius As System.Double
Dim Points As System.Object
Dim value As System.Boolean

value = instance.GetBendLineValues2(Up, Angle, Radius, Points)
```

### C#

```csharp
System.bool GetBendLineValues2(
   out System.bool Up,
   out System.double Angle,
   out System.double Radius,
   out System.object Points
)
```

### C++/CLI

```cpp
System.bool GetBendLineValues2(
   [Out] System.bool Up,
   [Out] System.double Angle,
   [Out] System.double Radius,
   [Out] System.Object^ Points
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Up`: True if the bend is up, false if the bend is down
- `Angle`: Angle of the bend
- `Radius`: Radius of the bend
- `Points`: Array of doubles (see Remarks)

### Return Value

True if the note is a bend note, false if not

## VBA Syntax

See [Note::GetBendLineValues2](ms-its:sldworksapivb6.chm::/Sldworks~Note~GetBendLineValues2.html).

## Remarks

Points will contain six (6) doubles (three (3) each for the start point and endpoint), one set for each segment in the bend line:

[ x, y, z, x, y, z ]

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
