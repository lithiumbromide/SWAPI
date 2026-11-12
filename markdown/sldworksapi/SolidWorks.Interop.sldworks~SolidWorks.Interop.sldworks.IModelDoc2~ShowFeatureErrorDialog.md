---
title: "ShowFeatureErrorDialog Property (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ShowFeatureErrorDialog"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowFeatureErrorDialog.html"
---

# ShowFeatureErrorDialog Property (IModelDoc2)

Gets or sets whether to display the feature error dialog.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowFeatureErrorDialog As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

instance.ShowFeatureErrorDialog = value

value = instance.ShowFeatureErrorDialog
```

### C#

```csharp
System.bool ShowFeatureErrorDialog {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowFeatureErrorDialog {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True displays an error dialog, false does not

## VBA Syntax

See [ModelDoc2::ShowFeatureErrorDialog](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ShowFeatureErrorDialog.html).

## Remarks

This property controls the display of error dialogs generated when an error occurs during a rebuild of a specific feature in the current SOLIDWORKS Design session. Use [ISldWorks::GetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetUserPreferenceToggle.html) or [ISldWorks::SetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html) to get or set swShowErrorsEveryRebuild, which controls the display of error dialogs generated when a rebuild warning error message is generated.

You can wrap the rebuild API call with the following code to suppress rebuild warning dialogs:

```vb
bValue = swApp.GetUserPreferenceToggle(swShowErrorsEveryRebuild)
swApp.SetUserPreferenceToggle swShowErrorsEveryRebuild, false
swModel.ForceRebuild3
swApp.SetUserPreferenceToggle swShowErrorsEveryRebuild, bValue
```

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ForceRebuild3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
