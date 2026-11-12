---
title: "PublishWithAllCustomProperties Property (IMBDSTEP242Data)"
project: "SOLIDWORKS API Help"
interface: "IMBDSTEP242Data"
member: "PublishWithAllCustomProperties"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data~PublishWithAllCustomProperties.html"
---

# PublishWithAllCustomProperties Property (IMBDSTEP242Data)

Gets or sets whether to publish all custom properties to the STEP 242 format.

## Syntax

### Visual Basic (Declaration)

```vb
Property PublishWithAllCustomProperties As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMBDSTEP242Data
Dim value As System.Boolean

instance.PublishWithAllCustomProperties = value

value = instance.PublishWithAllCustomProperties
```

### C#

```csharp
System.bool PublishWithAllCustomProperties {get; set;}
```

### C++/CLI

```cpp
property System.bool PublishWithAllCustomProperties {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to publish all custom properties, false to not

## VBA Syntax

See [MBDSTEP242Data::PublishWithAllCustomProperties](ms-its:sldworksapivb6.chm::/sldworks~MBDSTEP242Data~PublishWithAllCustomProperties.html).

## Examples

See the [IMBDSTEP242Data](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data.html) examples.

## See Also

[IMBDSTEP242Data Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data.html)
[IMBDSTEP242Data Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data_members.html)

## Availability

SOLIDWORKS 2025 SP03, Revision Number 33.3
