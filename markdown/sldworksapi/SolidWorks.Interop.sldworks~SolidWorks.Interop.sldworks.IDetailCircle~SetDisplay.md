---
title: "SetDisplay Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "SetDisplay"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetDisplay.html"
---

# SetDisplay Method (IDetailCircle)

Sets the display of the detail circle to a circle or to the profile.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDisplay( _
   ByVal Display As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim Display As System.Integer
Dim value As System.Boolean

value = instance.SetDisplay(Display)
```

### C#

```csharp
System.bool SetDisplay(
   System.int Display
)
```

### C++/CLI

```cpp
System.bool SetDisplay(
   System.int Display
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Display`: Display as defined by [swDetCircleShowType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDetCircleShowType_e.html)

### Return Value

True if setting the detail circle display is successful, false if not

## VBA Syntax

See [DetailCircle::SetDisplay](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~SetDisplay.html).

## Remarks

Use this method to display the detail circle or detail profile as a circle or as a profile.

| If... | Then... |
| --- | --- |
| Detail circle was originally set up as a circle | there is no profile. using this method to set display to swDetCirclePROFILE has no effect. this method returns false. |
| Style of the detail circle (see IDetailCircle::GetStyle ) is swDetViewBROKEN or swDetViewSTANDARD and the current detailing standard is ANSI | this method cannot set the display to swDetCirclePROFILE because the display must be a circle. |

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)
[IDetailCircle::GetStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetStyle.html)

## Availability

SOLIDWORKS 2004 SP1, Revision Number 12.1
