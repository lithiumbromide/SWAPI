---
title: "Render Model (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Render_Model_Example_VBNET.htm"
---

# Render Model (VB.NET)

This example shows how to use a ray-trace rendering engine to render a model and save the rendered image in BMP and HDR formats. You must have a Premium license to run this example.

'----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that:
' * specified part exists.
' * **c:\temp** exists.
' * ray-trace rendering engine is loaded in SOLIDWORKS Design.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. If prompted to use perspective views in renderings, click
' **Continue without Camera or Perspective**.
' 2. Changes the specified rendering options.
' 3. Creates **c:\temp\Filter_1.bmp** and **c:\temp\Filter_2.hdr** containing
' rendered images of the part.
' 4. Examine the Immediate window and **c:\temp**.
'
' NOTE: Rendering can take several minutes to complete.
'---------------------------------------------------------------------------
