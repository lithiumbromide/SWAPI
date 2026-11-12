---
title: "ReferencedConfiguration Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "ReferencedConfiguration"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReferencedConfiguration.html"
---

# ReferencedConfiguration Property (IView)

Gets or sets the configuration referenced by this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReferencedConfiguration As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.String

instance.ReferencedConfiguration = value

value = instance.ReferencedConfiguration
```

### C#

```csharp
System.string ReferencedConfiguration {get; set;}
```

### C++/CLI

```cpp
property System.String^ ReferencedConfiguration {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the configuration for the drawing view

## VBA Syntax

See [View::ReferencedConfiguration](ms-its:sldworksapivb6.chm::/sldworks~View~ReferencedConfiguration.html).

## Examples

[Get Configurations Referenced in View (C#)](Get_Configurations_Referenced_in_View_Example_CSharp.htm)
[Get Configurations Referenced in View (VB.NET)](Get_Configurations_Referenced_in_View_Example_VBNET.htm)
[Get Configurations Referenced in View (VBA)](Get_Configurations_Referenced_in_View_Example_VB.htm)

## Remarks

After changing the configuration, you must call [IModelDoc2::EditRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRebuild3.html) to see the changes.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetReferencedModelName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetReferencedModelName.html)
[IView::ReferencedDocument Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReferencedDocument.html)
[IView::ReferencedConfigurationID Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReferencedConfigurationID.html)
