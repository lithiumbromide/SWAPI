---
title: "GetStream Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetStream"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetStream.html"
---

# GetStream Method (IModelDocExtension)

Gets the handle for the specified stream.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStream( _
   ByVal StreamType As System.Integer, _
   ByRef ReadOnly As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim StreamType As System.Integer
Dim ReadOnly As System.Boolean
Dim value As System.Object

value = instance.GetStream(StreamType, ReadOnly)
```

### C#

```csharp
System.object GetStream(
   System.int StreamType,
   out System.bool ReadOnly
)
```

### C++/CLI

```cpp
System.Object^ GetStream(
   System.int StreamType,
   [Out] System.bool ReadOnly
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StreamType`: 1 = material stream
- `ReadOnly`: True if the stream is read-only, false if not

### Return Value

Pointer to the IUnknown interface for this stream

## VBA Syntax

See [ModelDocExtension::GetStream](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetStream.html).

## Remarks

To release the stream, call [IModelDocExtension::ReleaseStream](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~ReleaseStream.html).

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
