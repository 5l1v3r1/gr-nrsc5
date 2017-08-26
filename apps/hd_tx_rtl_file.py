#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Hd Tx Rtl File
# Generated: Fri Aug 25 20:35:57 2017
##################################################

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import math
import nrsc5


class hd_tx_rtl_file(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Hd Tx Rtl File")

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=2,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.nrsc5_psd_encoder_0 = nrsc5.psd_encoder('Title', 'Artist')
        self.nrsc5_pids_encoder_0 = nrsc5.pids_encoder('ABCD')
        self.nrsc5_l2_encoder_0 = nrsc5.l2_encoder()
        self.nrsc5_l1_fm_encoder_0 = nrsc5.l1_fm_encoder()
        self.nrsc5_hdc_encoder_0 = nrsc5.hdc_encoder(2, 64000)
        self.fft_vxx_0 = fft.fft_vcc(2048, False, (window.rectangular(2048)), True, 1)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((-1-1j, -1+1j, 1-1j, 1+1j, 0), 1)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('sample.wav', False)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, 2048)
        self.blocks_vector_source_x_0 = blocks.vector_source_c([math.sin(math.pi / 2 * i / 112) for i in range(112)] + [1] * (2048-112) + [math.cos(math.pi / 2 * i / 112) for i in range(112)], True, 1, [])
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 2048)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_gr_complex*2048, 2)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.5, ))
        self.blocks_keep_m_in_n_0 = blocks.keep_m_in_n(gr.sizeof_gr_complex, 2160, 4096, 0)
        self.blocks_interleave_0 = blocks.interleave(gr.sizeof_float*1, 1)
        self.blocks_float_to_uchar_0 = blocks.float_to_uchar()
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, 'hd-generated.raw', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_conjugate_cc_0 = blocks.conjugate_cc()
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_const_vxx_0_0 = blocks.add_const_vff((127.5, ))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.blocks_float_to_uchar_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_interleave_0, 1))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_interleave_0, 0))
        self.connect((self.blocks_conjugate_cc_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_float_to_uchar_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_interleave_0, 0), (self.blocks_add_const_vxx_0_0, 0))
        self.connect((self.blocks_keep_m_in_n_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_conjugate_cc_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_keep_m_in_n_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.nrsc5_hdc_encoder_0, 0))
        self.connect((self.blocks_wavfile_source_0, 1), (self.nrsc5_hdc_encoder_0, 1))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.nrsc5_hdc_encoder_0, 0), (self.nrsc5_l2_encoder_0, 0))
        self.connect((self.nrsc5_l1_fm_encoder_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.nrsc5_l2_encoder_0, 0), (self.nrsc5_l1_fm_encoder_0, 1))
        self.connect((self.nrsc5_pids_encoder_0, 0), (self.nrsc5_l1_fm_encoder_0, 0))
        self.connect((self.nrsc5_psd_encoder_0, 0), (self.nrsc5_l2_encoder_0, 1))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_multiply_const_vxx_0, 0))


def main(top_block_cls=hd_tx_rtl_file, options=None):

    tb = top_block_cls()
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
