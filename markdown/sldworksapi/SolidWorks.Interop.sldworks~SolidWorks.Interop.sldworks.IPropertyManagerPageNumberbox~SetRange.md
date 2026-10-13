---
title: "SetRange Method (IPropertyManagerPageNumberbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageNumberbox"
member: "SetRange"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~SetRange.html"
---

# SetRange Method (IPropertyManagerPageNumberbox)

Obsolete. Superseded by [PropertyManagerPageNumberbox::SetRange2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageNumberbox~SetRange2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetRange( _
   ByVal Units As System.Integer, _
   ByVal Minimum As System.Double, _
   ByVal Maximum As System.Double, _
   ByVal Increment As System.Double, _
   ByVal Inclusive As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageNumberbox
Dim Units As System.Integer
Dim Minimum As System.Double
Dim Maximum As System.Double
Dim Increment As System.Double
Dim Inclusive As System.Boolean

instance.SetRange(Units, Minimum, Maximum, Increment, Inclusive)
```

### C#

```csharp
void SetRange(
   System.int Units,
   System.double Minimum,
   System.double Maximum,
   System.double Increment,
   System.bool Inclusive
)
```

### C++/CLI

```cpp
void SetRange(
   System.int Units,
   System.double Minimum,
   System.double Maximum,
   System.double Increment,
   System.bool Inclusive
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Units`: Number box units as defined in [swNumberboxUnitType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNumberboxUnitType_e.html)
- `Minimum`: Number box minimum value
- `Maximum`: Number box maximum value
- `Increment`: Number box increment
- `Inclusive`: True sets the range as inclusive, false sets it as exclusive

## VBA Syntax

See [PropertyManagerPageNumberbox::SetRange](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageNumberbox~SetRange.html).

## Examples

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

## Remarks

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Show2.html) and [IProperytManagerPage2::Close](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Close.html).

## See Also

[IPropertyManagerPageNumberbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox.html)
[IPropertyManagerPageNumberbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
