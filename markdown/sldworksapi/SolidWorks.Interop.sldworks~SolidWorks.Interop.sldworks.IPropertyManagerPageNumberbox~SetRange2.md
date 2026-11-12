---
title: "SetRange2 Method (IPropertyManagerPageNumberbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageNumberbox"
member: "SetRange2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~SetRange2.html"
---

# SetRange2 Method (IPropertyManagerPageNumberbox)

Sets the range and increment for the slider.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetRange2( _
   ByVal Units As System.Integer, _
   ByVal Minimum As System.Double, _
   ByVal Maximum As System.Double, _
   ByVal Inclusive As System.Boolean, _
   ByVal Increment As System.Double, _
   ByVal FastIncr As System.Double, _
   ByVal SlowIncr As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageNumberbox
Dim Units As System.Integer
Dim Minimum As System.Double
Dim Maximum As System.Double
Dim Inclusive As System.Boolean
Dim Increment As System.Double
Dim FastIncr As System.Double
Dim SlowIncr As System.Double

instance.SetRange2(Units, Minimum, Maximum, Inclusive, Increment, FastIncr, SlowIncr)
```

### C#

```csharp
void SetRange2(
   System.int Units,
   System.double Minimum,
   System.double Maximum,
   System.bool Inclusive,
   System.double Increment,
   System.double FastIncr,
   System.double SlowIncr
)
```

### C++/CLI

```cpp
void SetRange2(
   System.int Units,
   System.double Minimum,
   System.double Maximum,
   System.bool Inclusive,
   System.double Increment,
   System.double FastIncr,
   System.double SlowIncr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Units`: Number box units as defined in [swNumberboxUnitType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNumberboxUnitType_e.html) (see **Remarks**)
- `Minimum`: Minimum value
- `Maximum`: Maximum value
- `Inclusive`: True sets the range as inclusive, false sets it as exclusive
- `Increment`: Increment value
- `FastIncr`: Fast increment value for scrolling and mouse-wheel
- `SlowIncr`: Slow increment value for scrolling and mouse-wheel

## VBA Syntax

See [PropertyManagerPageNumberbox::SetRange2](ms-its:sldworksapivb6.chm::/Sldworks~PropertyManagerPageNumberbox~SetRange2.html).

## Examples

[Create PropertyManager Page With Many Controls (VBA)](Create_PropertyManager_Page_With_Many_Controls_Example_VB.htm)

## Remarks

This method works while a PropertyManager page is displayed with these restrictions:

- You cannot change Units once the page is displayed. The Units parameter is ignored if specified while the page is displayed.
- If the range is changed to an invalid value by this method, then you must immediately call [IPropertyManagerPageNumberbox::Value](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageNumberbox~Value.html) and set a valid value to prevent displaying the dialog that requests the user to enter a valid value.

## See Also

[IPropertyManagerPageNumberbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox.html)
[IPropertyManagerPageNumberbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox_members.html)
[IPropertyManagerPageNumberbox::SetSliderParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~SetSliderParameters.html)
[IPropertyManagerPageNumberbox::DisplayedUnit Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~DisplayedUnit.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
