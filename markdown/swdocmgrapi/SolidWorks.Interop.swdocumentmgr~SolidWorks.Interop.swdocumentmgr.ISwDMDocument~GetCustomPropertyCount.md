---
title: "GetCustomPropertyCount Method (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "GetCustomPropertyCount"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyCount.html"
---

# GetCustomPropertyCount Method (ISwDMDocument)

Gets the number of custom properties for this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomPropertyCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
Dim value As System.Integer

value = instance.GetCustomPropertyCount()
```

### C#

```csharp
System.int GetCustomPropertyCount()
```

### C++/CLI

```cpp
System.int GetCustomPropertyCount();
```

### Return Value

Number of custom properties

## VBA Syntax

See [SwDMDocument::GetCustomPropertyCount](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~GetCustomPropertyCount.html).

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)
[ISwDMDocument::AddCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~AddCustomProperty.html)
[ISwDMDocument::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~DeleteCustomProperty.html)
[ISwDMDocument::GetCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomProperty.html)
[ISwDMDocument::GetCustomPropertyNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyNames.html)
[ISwDMDocument::SetCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~SetCustomProperty.html)
[ISwDMDocument3::GetAllCustomPropertyNamesAndValues Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument3~GetAllCustomPropertyNamesAndValues.html)
[ISwDMConfiguration::GetCustomPropertyCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyCount.html)
[ISwDMDocument17::GetCustomProperty2 Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17~GetCustomProperty2.html)
[ISwDMDocument5::GetCustomPropertyValues Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5~GetCustomPropertyValues.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
