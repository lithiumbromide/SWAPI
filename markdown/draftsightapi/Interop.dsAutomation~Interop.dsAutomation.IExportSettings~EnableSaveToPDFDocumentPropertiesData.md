---
title: "EnableSaveToPDFDocumentPropertiesData Property (IExportSettings)"
project: ""
interface: "IExportSettings"
member: "EnableSaveToPDFDocumentPropertiesData"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExportSettings~EnableSaveToPDFDocumentPropertiesData.html"
---

# EnableSaveToPDFDocumentPropertiesData Property (IExportSettings)

Gets or sets whether to add document properties data to the PDF.

## Syntax

### Visual Basic

```vb
Property EnableSaveToPDFDocumentPropertiesData As System.Boolean
```

### C#

```csharp
System.bool EnableSaveToPDFDocumentPropertiesData {get; set;}
```

### JScript

```
function get,set EnableSaveToPDFDocumentPropertiesData : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_EnableSaveToPDFDocumentPropertiesData();
__property void set_EnableSaveToPDFDocumentPropertiesData(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool EnableSaveToPDFDocumentPropertiesData {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True (default) to save document properties to the PDF, false to not

## Remarks

If this property is set to:

- false, all document properties are ignored.
- true, all document properties are set to empty strings.

## See Also

[IExportSettings Interface](Interop.dsAutomation~Interop.dsAutomation.IExportSettings.html)
[IExportSettings Members](Interop.dsAutomation~Interop.dsAutomation.IExportSettings_members.html)

## Availability

DraftSight 2018 SP2
