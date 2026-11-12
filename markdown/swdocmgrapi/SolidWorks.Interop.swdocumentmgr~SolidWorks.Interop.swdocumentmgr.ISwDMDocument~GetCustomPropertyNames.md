---
title: "GetCustomPropertyNames Method (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "GetCustomPropertyNames"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyNames.html"
---

# GetCustomPropertyNames Method (ISwDMDocument)

Gets the names of the custom properties for this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomPropertyNames() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
Dim value As System.Object

value = instance.GetCustomPropertyNames()
```

### C#

```csharp
System.object GetCustomPropertyNames()
```

### C++/CLI

```cpp
System.Object^ GetCustomPropertyNames();
```

### Return Value

Array of custom property name strings

## VBA Syntax

See [SwDMDocument::GetCustomPropertyNames](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~GetCustomPropertyNames.html).

## Examples

[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)

## Remarks

Call this method before calling [ISwDMDocument::DeleteCustomProperty](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~DeleteCustomProperty.html), [ISwDMDocument::GetCustomProperty](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetCustomProperty.html), or [ISwDMDocument::SetCustomProperty](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~SetCustomProperty.html).

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)
[ISwDMDocument::AddCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~AddCustomProperty.html)
[ISwDMDocument::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~DeleteCustomProperty.html)
[ISwDMDocument::GetCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomProperty.html)
[ISwDMDocument::GetCustomPropertyCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyCount.html)
[ISwDMDocument::SetCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~SetCustomProperty.html)
[ISwDMDocument3::GetAllCustomPropertyNamesAndValues Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument3~GetAllCustomPropertyNamesAndValues.html)
[ISwDMConfiguration::GetCustomPropertyNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyNames.html)
[ISwDMDocument5::GetCustomPropertyValues Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5~GetCustomPropertyValues.html)
[ISwDMDocument17::GetCustomProperty2 Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17~GetCustomProperty2.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
