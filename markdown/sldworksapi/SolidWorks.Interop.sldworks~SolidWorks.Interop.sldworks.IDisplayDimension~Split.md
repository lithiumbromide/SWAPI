---
title: "Split Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "Split"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Split.html"
---

# Split Property (IDisplayDimension)

Gets or sets whether to split a dual dimension above and below an unbroken dimension line (also called a leader).

## Syntax

### Visual Basic (Declaration)

```vb
Property Split As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

instance.Split = value

value = instance.Split
```

### C#

```csharp
System.bool Split {get; set;}
```

### C++/CLI

```cpp
property System.bool Split {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to split a dual dimension above and below an unbroken dimension line, false to not

## VBA Syntax

See [DisplayDimension::Split](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~Split.html).

## Examples

[Get Chamfer Display Dimension (C#)](Get_Chamfer_Display_Dimension_Example_CSharp.htm)
[Get Chamfer Display Dimension (VB.NET)](Get_Chamfer_Display_Dimension_Example_VBNET.htm)
[Get Chamfer Display Dimension (VBA)](Get_Chamfer_Display_Dimension_Example_VB.htm)

## Requirements

Setting this method to true only affects the following types of dual dimensions when the **Split when text position is "Solid Leader, Aligned Text"** option is selected in their **Tools > Options > Dimensions** dialog boxes:

- Arc Length
- Chamfer
- Diameter
- Linear
- Radius

To open the Help topic containing instructions on how to get and set the **Split when text position is "Solid Leader, Aligned Text"** option programmatically:

1. Click **Help** > **Use SOLIDWORKS Web Help**, if this menu item is checked.
2. Click **Help > API** **Help**.
3. Type **Document**.
4. Scroll down to the **properties** index subentry.
5. Scroll down to the **dimensions** index sub**-**subentry**.**
6. Double-click the type of dimension listed below **dimensions** whose dual dimension's **Split when text position is "Solid Leader, Aligned Text"** option you want to get or set.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetUseDocDual Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocDual.html)
[IDisplayDimension::SetDual Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetDual.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
