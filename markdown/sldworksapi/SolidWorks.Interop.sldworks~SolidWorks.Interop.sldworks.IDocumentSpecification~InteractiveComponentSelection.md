---
title: "InteractiveComponentSelection Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "InteractiveComponentSelection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~InteractiveComponentSelection.html"
---

# InteractiveComponentSelection Property (IDocumentSpecification)

Gets whether to display the Selective Open dialog, which allows the interactive user to either select and open specific components or open all of the displayed components.

## Syntax

### Visual Basic (Declaration)

```vb
Property InteractiveComponentSelection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.Boolean

instance.InteractiveComponentSelection = value

value = instance.InteractiveComponentSelection
```

### C#

```csharp
System.bool InteractiveComponentSelection {get; set;}
```

### C++/CLI

```cpp
property System.bool InteractiveComponentSelection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display the Selective Open dialog to the interactive user, false to not (default)

## VBA Syntax

See [DocumentSpecification::InteractiveComponentSelection](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~InteractiveComponentSelection.html).

## Remarks

This property is not valid for opening **3D**EXPERIENCE files using [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).

If this property is set to true, than any components added to the components list by [IDocumentSpecification::ComponentList](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDocumentSpecification~ComponentList.html) are ignored.

## See Also

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html)
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html)
[IDocumentSpecification::Selective Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Selective.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
