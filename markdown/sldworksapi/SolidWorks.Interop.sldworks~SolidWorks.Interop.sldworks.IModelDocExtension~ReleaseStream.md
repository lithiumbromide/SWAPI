---
title: "ReleaseStream Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "ReleaseStream"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReleaseStream.html"
---

# ReleaseStream Method (IModelDocExtension)

Releases a previously obtained stream.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReleaseStream( _
   ByVal StreamType As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim StreamType As System.Integer
Dim value As System.Boolean

value = instance.ReleaseStream(StreamType)
```

### C#

```csharp
System.bool ReleaseStream(
   System.int StreamType
)
```

### C++/CLI

```cpp
System.bool ReleaseStream(
   System.int StreamType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StreamType`: 1 = material stream

### Return Value

True if stream is released, false if not

## VBA Syntax

See [ModelDocExtension::ReleaseStream](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~ReleaseStream.html).

## Remarks

To obtain the stream, call [IModelDocExtension::GetStream](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetStream.html).

**VB Example**

This example illustrates attaching an XML document to a stream, and then releasing the stream.

```vb
Dim swApp As Object
Sub main()
Set swApp = Application.SldWorks
Dim docext As SldWorks.ModelDocExtension

Set docext = swApp.ActiveDoc.Extension

Dim xmldoc As MSXML2.DOMDocument
Set xmldoc = CreateObject("MSXML2.DOMDocument")
Dim stat As Boolean
Dim stream
Set stream = docext.GetStream(1, stat)
xmldoc.Load (stream)
docext.ReleaseStream (1)

xmldoc.Save ("C:\temp\xmlmat.xml")

End Sub
```

**C++ Example**

```vb
//--------
  CComPtr<IModelDocExtension> ext;
  m_iModelDoc2->get_Extension(&ext);
  LPSTREAM stream = NULL;
  VARIANT_BOOL access = 0;
  ext->IGetStream(1, &access, &stream);
  // Your code
  if (stream)
  {
  VARIANT_BOOL status;
  ext->IReleaseStream(1, &status);
  stream->Release();
  }
  //--------
```

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
