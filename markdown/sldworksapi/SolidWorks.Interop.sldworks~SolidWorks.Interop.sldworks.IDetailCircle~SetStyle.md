---
title: "SetStyle Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "SetStyle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetStyle.html"
---

# SetStyle Method (IDetailCircle)

Sets the style of the detail circle (for example, standard, broken, leader, no leader, or connected).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetStyle( _
   ByVal Style As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim Style As System.Integer
Dim value As System.Boolean

value = instance.SetStyle(Style)
```

### C#

```csharp
System.bool SetStyle(
   System.int Style
)
```

### C++/CLI

```cpp
System.bool SetStyle(
   System.int Style
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Style`: Style as defined by [swDetViewStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDetViewStyle_e.html)

### Return Value

True if setting the detail view style is successful, false if not

## VBA Syntax

See [DetailCircle::SetStyle](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~SetStyle.html).

## Remarks

This method sets different styles for the detail view display, following the detailing standard, as a broken circle, as a circle or profile with or without a leader to the detail label, or with a line connecting the detail circle or profile with the detail view.

This method automatically load the model for the detail view, if necessary, without prompting the user.

If the style of the detail circle is swDetViewBROKEN or swDetViewSTANDARD and the current detailing standard is ANSI, then this method automatically switches the detail circle or profile display to circle because a broken circle style requires a circle, not a profile.

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)
[IDetailCircle::GetStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetStyle.html)

## Availability

SOLIDWORKS 2004 SP1, Revision Number 12.1
