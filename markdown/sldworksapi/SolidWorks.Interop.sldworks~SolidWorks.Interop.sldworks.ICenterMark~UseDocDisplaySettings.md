---
title: "UseDocDisplaySettings Property (ICenterMark)"
project: "SOLIDWORKS API Help"
interface: "ICenterMark"
member: "UseDocDisplaySettings"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~UseDocDisplaySettings.html"
---

# UseDocDisplaySettings Property (ICenterMark)

Gets or sets whether to use the document defaults for this center mark's display settings.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseDocDisplaySettings As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterMark
Dim value As System.Boolean

instance.UseDocDisplaySettings = value

value = instance.UseDocDisplaySettings
```

### C#

```csharp
System.bool UseDocDisplaySettings {get; set;}
```

### C++/CLI

```cpp
property System.bool UseDocDisplaySettings {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True uses the document defaults, false does not

## VBA Syntax

See [CenterMark::UseDocDisplaySettings](ms-its:sldworksapivb6.chm::/sldworks~CenterMark~UseDocDisplaySettings.html).

## Examples

[List Center Marks in Drawing (VBA)](List_Center_Marks_in_Drawing_Example_VB.htm)

## Remarks

You can use the following user-preference methods to get or set these document defaults:

- [IModelDocExtension::SetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SetUserPreferenceToggle.html) or [IModelDocExtension::GetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceToggle.html) - swDetailingCenterMarkShowLines, swDetailingNoOptionSpecified
- [IModelDocExtension::SetUserPreferenceDouble](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SetUserPreferenceDouble.html) or [IModelDocExtension::GetUserPreferenceDouble](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceDouble.html) - swDetailingCenterMarkSize, swDetailingNoOptionSpecified

## See Also

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
