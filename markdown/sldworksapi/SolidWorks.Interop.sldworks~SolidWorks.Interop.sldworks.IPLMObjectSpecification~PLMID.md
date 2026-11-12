---
title: "PLMID Property (IPLMObjectSpecification)"
project: "SOLIDWORKS API Help"
interface: "IPLMObjectSpecification"
member: "PLMID"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPLMObjectSpecification~PLMID.html"
---

# PLMID Property (IPLMObjectSpecification)

Gets or sets the ID of a [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm) document.

## Syntax

### Visual Basic (Declaration)

```vb
Property PLMID As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPLMObjectSpecification
Dim value As System.String

instance.PLMID = value

value = instance.PLMID
```

### C#

```csharp
System.string PLMID {get; set;}
```

### C++/CLI

```cpp
property System.String^ PLMID {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Document ID

## VBA Syntax

See [PLMObjectSpecification::PLMID](ms-its:sldworksapivb6.chm::/sldworks~PLMObjectSpecification~PLMID.html).

## Examples

See the [IPLMObjectSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPLMObjectSpecification.html) examples.

## See Also

[IPLMObjectSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPLMObjectSpecification.html)
[IPLMObjectSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPLMObjectSpecification_members.html)

## Availability

SOLIDWORKS 2020 SP3.1, Revision Number 28.3.1
