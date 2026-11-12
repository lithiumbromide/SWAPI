---
title: "OpenDocument2 Method (IApplication)"
project: ""
interface: "IApplication"
member: "OpenDocument2"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~OpenDocument2.html"
---

# OpenDocument2 Method (IApplication)

Opens the specified document.

## Syntax

### Visual Basic

```vb
Function OpenDocument2( _
   ByVal PathName As System.String, _
   ByVal Option As dsDocumentOpenOption_e, _
   ByVal EncodingId As dsEncoding_e _
) As Document
```

### C#

```csharp
Document OpenDocument2(
   System.string PathName,
   dsDocumentOpenOption_e Option,
   dsEncoding_e EncodingId
)
```

### JScript

```
function OpenDocument2(
   PathName : System.String,
   Option : dsDocumentOpenOption_e,
   EncodingId : dsEncoding_e
) : Document;
```

### Managed Extensions for C++

```
Document* OpenDocument2(
   System.string* PathName,
   dsDocumentOpenOption_e Option,
   dsEncoding_e EncodingId
)
```

### C++/CLI

```cpp
Document^ OpenDocument2(
   System.String^ PathName,
   dsDocumentOpenOption_e Option,
   dsEncoding_e EncodingId
)
```

### Parameters

- `PathName`: Path and file name of document to open
- `Option`: Mode in which to open the document as defined in [dsDocumentOpenOption_e](Interop.dsAutomation~interop.dsAutomation.dsDocumentOpenOption_e.html)
- `EncodingId`: Encoding as defined in [dsEncoding_e](Interop.dsAutomation~Interop.dsAutomation.dsEncoding_e.html)

### Return Value

[Document](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)

## Examples

[Fire Application and Document Events (C#)](Fire_Application_and_Document_Events_Example_CSharp.htm)
[Fire Application and Document Events (VB.NET)](Fire_Application_and_Document_Events_Example_VBNET.htm)
[Fire Application and Document Events (VBA)](Fire_Application_and_Document_Events_Example_VBA.htm)
[Get and Set Hatch Pattern Data (C#)](Get_and_Set_Hatch_Pattern_Data_Example_CSharp.htm)
[Get and Set Hatch Pattern Data (VB.NET)](Get_and_Set_Hatch_Pattern_Data_Example_VBNET.htm)
[Get and Set Hatch Pattern Data (VBA)](Get_and_Set_Hatch_Pattern_Data_Example_VBA.htm)

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)

## Availability

V1R1.3
