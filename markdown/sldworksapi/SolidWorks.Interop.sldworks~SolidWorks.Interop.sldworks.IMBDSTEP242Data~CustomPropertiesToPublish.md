---
title: "CustomPropertiesToPublish Property (IMBDSTEP242Data)"
project: "SOLIDWORKS API Help"
interface: "IMBDSTEP242Data"
member: "CustomPropertiesToPublish"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data~CustomPropertiesToPublish.html"
---

# CustomPropertiesToPublish Property (IMBDSTEP242Data)

Gets or sets the model's custom properties to export to the STEP 242 format.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomPropertiesToPublish As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMBDSTEP242Data
Dim value As System.Object

instance.CustomPropertiesToPublish = value

value = instance.CustomPropertiesToPublish
```

### C#

```csharp
System.object CustomPropertiesToPublish {get; set;}
```

### C++/CLI

```cpp
property System.Object^ CustomPropertiesToPublish {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of custom properties

## VBA Syntax

See [MBDSTEP242Data::CustomPropertiesToPublish](ms-its:sldworksapivb6.chm::/sldworks~MBDSTEP242Data~CustomPropertiesToPublish.html).

## Examples

See the [IMBDSTEP242Data](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data.html) examples.

## Remarks

This property is valid only if [IMBDSTEP242Data::PublishWithAllCustomProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data~PublishWithAllCustomProperties.html) is set to false.

## See Also

[IMBDSTEP242Data Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data.html)
[IMBDSTEP242Data Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data_members.html)

## Availability

SOLIDWORKS 2025 SP03, Revision Number 33.3
