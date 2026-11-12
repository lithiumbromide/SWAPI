---
title: "ReferencedConfigurationID Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "ReferencedConfigurationID"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReferencedConfigurationID.html"
---

# ReferencedConfigurationID Property (IView)

Gets the persistent reference ID of the configuration referenced in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReferencedConfigurationID As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.ReferencedConfigurationID
```

### C#

```csharp
System.int ReferencedConfigurationID {get;}
```

### C++/CLI

```cpp
property System.int ReferencedConfigurationID {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Referenced configuration's persistent reference ID

## VBA Syntax

See [View::ReferencedConfigurationID](ms-its:sldworksapivb6.chm::/sldworks~View~ReferencedConfigurationID.html).

## Examples

[Get Configurations Referenced in View (C#)](Get_Configurations_Referenced_in_View_Example_CSharp.htm)
[Get Configurations Referenced in View (VB.NET)](Get_Configurations_Referenced_in_View_Example_VBNET.htm)
[Get Configurations Referenced in View (VBA)](Get_Configurations_Referenced_in_View_Example_VB.htm)

## Remarks

See [Persistent Reference IDs](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm) for more information.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetReferencedModelName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetReferencedModelName.html)
[IView::ReferencedConfiguration Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReferencedConfiguration.html)
[IView::ReferencedDocument Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReferencedDocument.html)
[IModelDocExtension::GetObjectByPersistReference3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetObjectByPersistReference3.html)
[IModelDocExtension::GetPersistReference3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReference3.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
