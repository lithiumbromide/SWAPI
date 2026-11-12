---
title: "LinkParentConfiguration Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "LinkParentConfiguration"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~LinkParentConfiguration.html"
---

# LinkParentConfiguration Property (IView)

Gets or sets whether to link a projected or auxiliary view with the parent configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Property LinkParentConfiguration As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

instance.LinkParentConfiguration = value

value = instance.LinkParentConfiguration
```

### C#

```csharp
System.bool LinkParentConfiguration {get; set;}
```

### C++/CLI

```cpp
property System.bool LinkParentConfiguration {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to link a projected or auxiliary view with the parent configuration, false to not

## VBA Syntax

See [View::LinkParentConfiguration](ms-its:sldworksapivb6.chm::/sldworks~View~LinkParentConfiguration.html).

## Examples

[Link Projected View to Parent Configuration (C#)](Link_Projected_View_to_Parent_Configuration_Example_CSharp.htm)
[Link Projected View to Parent Configuration (VB.NET)](Link_Projected_View_to_Parent_Configuration_Example_VBNET.htm)
[Link Projected View to Parent Configuration (VBA)](Link_Projected_View_to_Parent_Configuration_Example_VB.htm)

## Remarks

After setting this property, call [IModelDoc2::EditRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRebuild3.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
