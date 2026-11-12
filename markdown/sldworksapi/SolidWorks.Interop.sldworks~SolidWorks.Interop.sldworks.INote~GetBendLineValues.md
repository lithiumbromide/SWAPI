---
title: "GetBendLineValues Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetBendLineValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBendLineValues.html"
---

# GetBendLineValues Method (INote)

Obsolete. Superseded by [INote::GetBendLineValues2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetBendLineValues2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBendLineValues( _
   ByRef Up As System.Boolean, _
   ByRef Angle As System.Double, _
   ByRef Radius As System.Double, _
   ByRef StartPt As MathPoint, _
   ByRef EndPt As MathPoint _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim Up As System.Boolean
Dim Angle As System.Double
Dim Radius As System.Double
Dim StartPt As MathPoint
Dim EndPt As MathPoint
Dim value As System.Boolean

value = instance.GetBendLineValues(Up, Angle, Radius, StartPt, EndPt)
```

### C#

```csharp
System.bool GetBendLineValues(
   out System.bool Up,
   out System.double Angle,
   out System.double Radius,
   out MathPoint StartPt,
   out MathPoint EndPt
)
```

### C++/CLI

```cpp
System.bool GetBendLineValues(
   [Out] System.bool Up,
   [Out] System.double Angle,
   [Out] System.double Radius,
   [Out] MathPoint^ StartPt,
   [Out] MathPoint^ EndPt
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Up`: True if the bend is up, false if the bend is down
- `Angle`: Angle of the bend
- `Radius`: Radius of the bend
- `StartPt`: Start [point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) of the bend line
- `EndPt`: End [point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) of the bend line

### Return Value

True if the note is a bend note, false if not

## VBA Syntax

See [Note::GetBendLineValues](ms-its:sldworksapivb6.chm::/sldworks~Note~GetBendLineValues.html).

## Examples

[Get Bend Line Note Values (VBA)](Get_Bend_Line_Note_Values_Example_VB.htm)

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::IsBendLineNote Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsBendLineNote.html)

## Availability

SolidWorisk 2007 SP2, Revision Number 15.2
